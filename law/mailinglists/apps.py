from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MailingListsConfig(AppConfig):
    name = 'law.mailinglists'
    verbose_name = _('Mailing Lists')
