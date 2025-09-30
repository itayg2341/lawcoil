from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContactConfig(AppConfig):
    name = 'law.contact'
    verbose_name = _('Site Feedback')
