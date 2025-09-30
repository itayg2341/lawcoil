from django.db import models
from django.utils.translation import gettext_lazy as _


class FeedbackMessage(models.Model):

    name = models.CharField(_('Name'), max_length=200)
    email = models.EmailField(_('Email'), max_length=250)
    phone = models.CharField(_('Phone'), blank=True, null=True, max_length=40)
    role = models.CharField(_('Role'), blank=True, null=True, max_length=100)
    organization = models.CharField(_('Organization'), blank=True, null=True,
                                    max_length=200)
    content = models.TextField(_('Content'))
    received_at = models.DateTimeField(_('Received At'), db_index=True,
                                       blank=True, auto_now_add=True)

    class Meta:
        ordering = ('received_at', )
        verbose_name = _('Feedback Message')
        verbose_name_plural = _('Feedback Messages')
