from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RedirectsConfig(AppConfig):
    name = 'law.redirects'
    verbose_name = _('URL Redirects')
