from ckeditor.fields import RichTextField
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _, override


class Page(models.Model):
    """A simple page object"""

    title = models.CharField(_('Title'), max_length=196)
    slug = models.SlugField(_('Slug'), max_length=60, db_index=True)
    language = models.CharField(_('Language'), max_length=5, db_index=True,
                                choices=settings.LANGUAGES)
    published = models.BooleanField(_('Published'), default=True)
    content = RichTextField(_('Content'))
    template = models.CharField(_('Optional Template'), max_length=200,
                                blank=True, null=True)

    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')
        unique_together = ('language', 'slug')

    def __str__(self):
        return self.title

        def get_absolute_url(self):
            with override(self.language):
                url = reverse('pages:page', kwargs={'slug': self.slug})
            return url
