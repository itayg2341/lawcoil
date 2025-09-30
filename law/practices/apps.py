from django import apps
from django.utils.translation import gettext_lazy as _


class AppConfig(apps.AppConfig):

    name = 'law.practices'
    verbose_name = _('Practice Areas')
