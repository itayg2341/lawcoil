from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LinksConfig(AppConfig):
    name = 'law.links'
    verbose_name = _('Links')
