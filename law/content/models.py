from datetime import datetime, timedelta
from urllib.parse import quote

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.conf import settings
from django.contrib.sites.models import Site
from django.core import signing
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.html import strip_tags, format_html
from django.utils.translation import gettext_lazy as _, override

from law.contributors.models import Contributor
from law.users.models import User
from .const import CONTENT_TYPE
from .managers import (ContentCategoryManager, CommonContentManager,
                       ArticleManager, NewsItemManager, ComputerLawManager,
                       LegislationManager)

WORDS_PER_MINUTE = 200
CATEGORIES_CACHE_KEY = 'generic_categories_{}'


class ContentCategory(models.Model):
    """A generic category which can span News, Articles etc"""

    name = models.CharField(_('Name'), max_length=200, db_index=True)
    slug = models.SlugField(_('Slug'))
    color = ColorField(_('Color'), default='#FF0000')
    icon_css_class = models.CharField(_('CSS icon class'), max_length=40,
                                      blank=True)
    language = models.CharField(_('Language'), max_length=5, db_index=True,
                                choices=settings.LANGUAGES)
    is_hot = models.BooleanField(_('Hot Topic'), default=False, db_index=True)
    followers = models.ManyToManyField(User, related_name='categories')

    objects = ContentCategoryManager()

    class Meta:
        ordering = ['name']
        verbose_name = _('Content Category')
        verbose_name_plural = _('Content Categories')

    def __str__(self):
        return self.name

    def published_items(self):
        """docstring for published_items"""
        return self.items.filter(is_published=True)

    def get_absolute_url(self):
        from django.urls import reverse
        with override(self.language):
            url = reverse('topics:category', kwargs={'cat_slug': self.slug})
        return url

    @classmethod
    def get_cached_categories(cls, language):
        key = CATEGORIES_CACHE_KEY.format(language)

        categories = cache.get(key)

        if categories is None:
            categories = cls.objects.filter(language=language).order_by('name')
            cache.set(key, categories, None)

        return categories


@receiver(post_save, sender=ContentCategory)
def invalidate_cache_on_save(sender, **kwargs):
    keys = [CATEGORIES_CACHE_KEY.format(lang_code) for (lang_code, desc) in
            settings.LANGUAGES]
    cache.delete_many(keys)


CONTENT_TYPE_CHOICES = [(x.value, x.name) for x in list(CONTENT_TYPE)]
CONTENT_TYPE_DICT = dict(CONTENT_TYPE_CHOICES)


class CommonContent(models.Model):
    """common model for content on the site"""
    title = models.CharField(_('Title'), max_length=196)
    slug = models.SlugField(_('Slug'), max_length=60)
    created_at = models.DateTimeField(_('Created At'), default=timezone.now,
                                      db_index=True)
    content = RichTextField(_('Content'))
    language = models.CharField(_('Language'), max_length=5, db_index=True,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGES[0][0])
    published = models.BooleanField(_('Published'), default=False,
                                    db_index=True)
    contributors = models.ManyToManyField(
        Contributor, related_name='%(class)s', verbose_name=_('Contributors'))

    ctype = models.PositiveIntegerField(_('Content Type'),
                                        choices=CONTENT_TYPE_CHOICES)
    reading_time = models.IntegerField(_('Reading Time'), blank=True)

    # Article item
    sub_title = models.CharField(_('Sub Title'), max_length=255, blank=True,
                                 null=True)
    short_desc = RichTextField(_('Short Description'), blank=True, null=True)

    # Computer law item
    attachment = models.FileField(_('Attached file'), upload_to='computer-law',
                                  max_length=255, blank=True, null=True)
    url = models.CharField(_('Link to'), max_length=200, blank=True, null=True)

    categories = models.ManyToManyField(ContentCategory,
                                        verbose_name=_('Categories'),
                                        related_name='items')
    saved_by = models.ManyToManyField(User, related_name='items')

    email_notified = models.BooleanField(_('Email words notification sent'),
                                         default=False)

    objects = CommonContentManager()

    class Meta:
        ordering = ['-created_at']
        index_together = [
            ['language', 'ctype', 'created_at']
        ]
        unique_together = ('language', 'ctype', 'slug')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """Calculate reading time on save"""
        words = len(strip_tags(self.content).split())
        minutes = words // WORDS_PER_MINUTE

        self.reading_time = minutes

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<CommonContent({}): {}>'.format(CONTENT_TYPE_DICT[self.ctype],
                                                self.title)

    @property
    def category(self):
        return self.categories.first()

    def get_absolute_url(self):
        from django.urls import reverse
        with override(self.language):
            created_at = self.created_at
            kwargs = {
                'year': str(created_at.year).zfill(2),
                'month': str(created_at.month).zfill(2),
                'day': str(created_at.day).zfill(2),
                'slug': self.slug,
                'content_type': self.url_content_type,
            }
            url = reverse('content:detail', kwargs=kwargs)
        return url

    @property
    def url_content_type(self):
        return CONTENT_TYPE_DICT[self.ctype].replace('_', '-')

    def get_verbose_name(self):
        content_type = CONTENT_TYPE_DICT[self.ctype]
        return CommonContent.objects.get_verbose_name_for_content_type(
            content_type)

    def facebook_check_link(self):
        base_link = 'https://developers.facebook.com/tools/debug/og/object?q='
        domain = Site.objects.get_current().domain
        content_link = 'https://' + domain + self.get_absolute_url()
        return format_html(
            '<a class="button-link" href="{}{}" target="_blank" '
            'rel="noopener">{}</a>',
            base_link,
            quote(content_link, safe=''),
            _('Facebook')
        )
    facebook_check_link.short_description = _('Facebook')

    def get_similar(self, total=3):
        """Get up to `total` similar items for last 3 months.
        :returns: QuerySet of matching CommonContent intsances

        """
        category_pks = self.categories.values_list('pk', flat=True)
        items_pks =  (self.categories.through.objects
                          .filter(contentcategory_id__in=category_pks)
                          .values_list('pk', flat=True)
                          .distinct())
        last_3_months = datetime.today() - timedelta(days=90)
        related_qs = (CommonContent.objects
                        .filter(published=True, ctype=self.ctype,
                                language=self.language, pk__in=items_pks,
                                created_at__gte=last_3_months)
                        .exclude(pk=self.pk)
                        .select_related()
                        .order_by('?')[:total])
        return related_qs

    def get_annotation_uri(self):

        signing_uri_obj = {
            'pk': self.pk,
        }

        return signing.dumps(signing_uri_obj, key=settings.PASSWORD_ENC_KEY)


class Article(CommonContent):

    objects = ArticleManager()

    class Meta:
        proxy = True
        ordering = ['-created_at']
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')


class NewsItem(CommonContent):

    objects = NewsItemManager()

    class Meta:
        proxy = True
        ordering = ['-created_at']
        verbose_name = _('News Item')
        verbose_name_plural = _('News Items')


class ComputerLaw(CommonContent):

    objects = ComputerLawManager()

    class Meta:
        proxy = True
        ordering = ['-created_at']
        verbose_name = _('Computer Law')
        verbose_name_plural = _('Computer Laws')


class Legislation(CommonContent):

    objects = LegislationManager()

    class Meta:
        proxy = True
        ordering = ['-created_at']
        verbose_name = _('Legislation')
        verbose_name_plural = _('Legislations')
