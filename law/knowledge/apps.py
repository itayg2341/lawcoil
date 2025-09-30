from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class KnowledgeConfig(AppConfig):
    name = 'law.knowledge'
    verbose_name = _('Knowledge Centers')
