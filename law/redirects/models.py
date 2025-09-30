from django.db import models
from django.utils.translation import gettext_lazy as _


class Redirects(models.Model):
    "Redirect urls to other ones"

    from_url = models.CharField(_('From URL'), max_length=255, unique=True)
    to_url = models.CharField(_('To URL'), max_length=255)
    comment = models.TextField(_('Comment'), blank=True, null=True)

    class Meta:
        verbose_name = _('URL Redirect')
        verbose_name = _('URL Redirects')

    @staticmethod
    def ensure_slashes(value):
        if not value.startswith('/'):
            value = '/' + value

        if not value.endswith('/'):
            value = value + '/'

        return value

    def save(self, *args, **kwargs):
        "Ensure we have slashes at beginging and end"

        self.from_url = self.ensure_slashes(self.from_url)
        self.to_url = self.ensure_slashes(self.to_url)

        super().save(*args, **kwargs)
