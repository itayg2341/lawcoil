from ckeditor.fields import RichTextField
from django.conf import settings
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _, override
from functools import lru_cache
from mptt.fields import TreeManyToManyField
from mptt.models import MPTTModel, TreeForeignKey


LINKS_CACHE_KEY = 'link_categories_{}'


class Category(MPTTModel):
    lang = models.CharField(_('Language'), max_length=10,
                            choices=settings.LANGUAGES, db_index=True)
    name = models.CharField(_('Name'), unique=True, max_length=128)
    desc = RichTextField(_('Description'), blank=True, null=True)
    slug = models.SlugField(_('Slug'))
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        db_index=True,
        verbose_name=_('Parent'),
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = _('Links category')
        verbose_name_plural = _('Links categories')
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    @property
    @lru_cache(maxsize=2)
    def ancestors(self):
        return list(self.get_ancestors(ascending=False, include_self=True))[1:]

    @property
    @lru_cache(maxsize=2)
    def slugs_path(self):
        """Calculates the slugs path to this category from root"""

        slugs_without_root = [x.slug for x in self.ancestors]

        return '/'.join(slugs_without_root)

    def get_absolute_url(self):
        from django.urls import reverse

        with override(self.lang):
            url = reverse('links:category',
                          kwargs={'slugs_path': self.slugs_path + '/'})
        return url

    @classmethod
    def get_cached_categories(cls, language):
        key = LINKS_CACHE_KEY.format(language)

        categories = cache.get(key)


        if categories is None:
            root = cls.objects.root_nodes().filter(lang=language).first()
            if root is not None:
                categories = root.get_children()
            else:
                categories = cls.objects.none()
            cache.set(key, categories, None)

        return categories


@receiver(post_save, sender=Category)
def invalidate_cache_on_save(sender, **kwargs):
    keys = [LINKS_CACHE_KEY.format(lang_code) for (lang_code, desc) in
            settings.LANGUAGES]
    cache.delete_many(keys)


class Link(models.Model):
    engname = models.CharField(_('English name'), max_length=200, blank=True,
                               null=True, db_index=True)
    hebname = models.CharField(_('Hebrew name'), max_length=200, blank=True,
                               null=True, db_index=True)
    url = models.URLField(_('URL'), max_length=255, blank=True, null=True)
    engdesc = RichTextField(_('English description'), blank=True, null=True)
    hebdesc = RichTextField(_('Hebrew description'), blank=True, null=True)
    categories = TreeManyToManyField(Category, related_name='links',
                                     verbose_name=_('Categories'))
    created_at = models.DateField(_('Created at'), blank=True, null=True,
                                  default=timezone.now, db_index=True)
    online = models.BooleanField(_('Online'), default=True, db_index=True)

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')

    def __str__(self):
        return '{} {}'.format(self.engname, self.hebname)
