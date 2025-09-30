from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PhotosConfig(AppConfig):
    name = 'law.photos'
    verbose_name = _('Photos')
