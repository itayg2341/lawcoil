from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

from law.lawyers.models import Lawyer


class Contributor(models.Model):
    name = models.CharField(_('Name'), max_length=128)
    is_default = models.BooleanField(_('Default ?'), default=False)
    short_desc = RichTextField(_('Short Description'), blank=True, null=True)
    small_photo = models.ImageField(_('Small Photo'),
                                    upload_to="contributors/",
                                    blank=True, null=True,
                                    help_text=_('Small photo (125x125)'))
    link = models.URLField(_('Link to author'), blank=True, null=True)
    show_link = models.BooleanField(_('Show link'), default=False)
    lawyer = models.ForeignKey(
        Lawyer,
        blank=True,
        null=True,
        verbose_name=_('Lawyer'),
        on_delete=models.SET_NULL
    )
    order = models.IntegerField(_('Order'), blank=True, default=10,
                                db_index=True)

    class Meta:
        verbose_name = _('Contributor')
        verbose_name_plural = _('Contributors')
        ordering = ('order', 'name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('contributors:contributor', kwargs={'pk': self.pk})

    @property
    def normalized_link(self):
        if self.lawyer:
            return self.lawyer.get_absolute_url()
        return self.link or self.get_absolute_url()

    @property
    def normalized_photo(self):
        if self.lawyer:
            return self.lawyer.profile_photo
        return self.small_photo
