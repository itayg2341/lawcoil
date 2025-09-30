from ckeditor.fields import RichTextField
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _, override


class PracticeArea(models.Model):

    title = models.CharField(_('Title'), max_length=200)
    language = models.CharField(_('Language'), max_length=5, db_index=True,
                                choices=settings.LANGUAGES)
    slug = models.SlugField(_('Slug'), max_length=60)
    content = RichTextField(_('Content'))
    published = models.BooleanField(_('Published'), default=True, db_index=True)
    order = models.IntegerField(_('Order'), default=1, db_index=True)

    class Meta:
        verbose_name = _('Practice Area')
        verbose_name_plural = _('Practice Areas')
        ordering = ('language', 'order')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        with override(self.language):
            url = reverse('practices:practice', kwargs={'slug': self.slug})
        return url
