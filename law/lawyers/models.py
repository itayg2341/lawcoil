from ckeditor.fields import RichTextField
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _, override
from easy_thumbnails.fields import ThumbnailerImageField


class Lawyer(models.Model):

    language = models.CharField(_('Language'), max_length=5, db_index=True,
                                choices=settings.LANGUAGES)
    name = models.CharField(_('Name'), max_length=100)
    title = models.CharField(_('Title'), max_length=200, blank=True, null=True)
    slug = models.SlugField(_('Slug'), max_length=60, db_index=True)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Phone'), max_length=100)
    short_description = RichTextField(_('Short Description'))
    description = RichTextField(_('Description'))
    profile_photo = ThumbnailerImageField(
        _('Small Profile Photo'), upload_to='lawyers',
        help_text="Cropped to 200x200",
        resize_source={'size': (200, 200), 'crop': True})
    large_photo = models.ImageField(_('Large Photo'), upload_to='lawyers',
                                    help_text="Best 1280x532")
    order = models.IntegerField(_('Order'), default=0, db_index=True)

    class Meta:
        verbose_name = _('Lawyer')
        verbose_name_plural = _('Group Lawyers')
        ordering = ('language', 'order')

    def get_absolute_url(self):
        with override(self.language):
            url = reverse('lawyers:lawyer', kwargs={'slug': self.slug})
        return url

    def __str__(self):
        return self.name
