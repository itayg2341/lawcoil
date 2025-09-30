from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AnnotationsConfig(AppConfig):
    name = 'law.annotations'
    verbose_name = _('Annotations')
