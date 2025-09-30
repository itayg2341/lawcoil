from django.db import models
from django.utils.translation import gettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils.safestring import mark_safe


class WidePhoto(models.Model):

    """Wide aspect ration photo"""
    photo = ThumbnailerImageField(
        _('Photo'), upload_to='wide_photos',
        resize_source={'size': (582, 420), 'crop': True})

    def photo_img(self):
        if self.photo:
            return mark_safe('<img src="%s" style="width:100px"/>' % self.photo.url)
        else:
            return 'No Photo'
    photo_img.short_description = 'Thumb'

    class Meta:
        verbose_name = _('Wide Photo')
        verbose_name_plural = _('Wide Photos')

    def __str__(self):
        try:
            return self.photo.url
        except AttributeError:
            return '<Wide Photo>'


class NarrowPhoto(models.Model):

    """Wide aspect ration photo"""
    photo = ThumbnailerImageField(
        _('Photo'), upload_to='narrow_photos',
        resize_source={'size': (269, 615), 'crop': True})

    class Meta:
        verbose_name = _('Narrow Photo')
        verbose_name_plural = _('Narrow Photos')

    def photo_img(self):
        if self.photo:
            return mark_safe('<img src="%s" style="height:100px"/>' % self.photo.url)
        else:
            return 'No Photo'

    photo_img.short_description = 'Thumb'

    def __str__(self):
        try:
            return self.photo.url
        except AttributeError:
            return '<Narrow Photo>'
