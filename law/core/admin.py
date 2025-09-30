from allauth.account.models import EmailAddress, EmailConfirmation
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from django.contrib import admin
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _


admin.site.site_header = _('law.co.il administration')

# Unsubscribe some models

from django.contrib.admin.sites import NotRegistered

for model in [SocialToken, SocialAccount, SocialApp, Site, EmailAddress, EmailConfirmation]:
	try:
		admin.site.unregister(model)
	except NotRegistered:
		pass
