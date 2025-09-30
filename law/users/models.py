# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from cryptography.fernet import Fernet
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

 
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    encrypted_password = models.BinaryField(_("Encrypted Password"),
                                            blank=True)
    organization = models.CharField(_('Organization'), blank=True, null=True,
                                    max_length=200)
    role = models.CharField(_('Role'), blank=True, null=True, max_length=100)
    phone = models.CharField(_('Phone'), blank=True, null=True, max_length=40)
    address = models.CharField(_('Address'), blank=True, null=True,
                               max_length=200)
    avatar = ThumbnailerImageField(
        _('Avatar'), blank=True, null=True, upload_to='avatars',
        resize_source={'size': (100, 100), 'crop': True})

    watch_words = models.TextField(
        _('Watch words'), blank=True, null=True, max_length=300,
        help_text=_('Receive an email when a published article or news item '
                    'contains a word or expression. Each word or expression in '
                    'a separate line, minimum length is 4 characters.')
    )

    send_newsletters = models.BooleanField(_("Send newsletters?"), default=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def set_password(self, raw_password):
        """Ensures encrypted password is stored as well"""
        super().set_password(raw_password)
        # Fernet requires a 32-byte url-safe base64 key
        key = settings.PASSWORD_ENC_KEY.encode()
        f = Fernet(key)
        self.encrypted_password = f.encrypt(raw_password.encode())

    def get_saved_item(self, item):
        """Checks if the user has item in his saved content

        if it does, returns the CommonContent instance, otherwise None

        :return: CommonContent instance or None
        """
        return self.items.filter(language=item.language, slug=item.slug).first()


class ShareContact(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'),
                             related_name='share_contacts',
                             on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=255)
    email = models.EmailField(_('Email'), max_length=255)

    class Meta:
        verbose_name = _('Share Contact')
        verbose_name_plural = _('Share Contacts')
        unique_together = ('user', 'email')


class ProxyGroup(Group):

    class Meta:
        proxy = True
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
