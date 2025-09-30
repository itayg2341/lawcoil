from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from law.content.models import (ContentCategory, CONTENT_TYPE_CHOICES,
                                CommonContent)
from law.users.models import User

SEND_DAYS_CHOICES = (
    (0, _('Do not send by days')),
    (1, _('1 Days')),
    (2, _('2 Days')),
    (3, _('3 Days')),
    (4, _('4 Days')),
    (5, _('5 Days')),
    (6, _('6 Days')),
    (7, _('7 Days')),
    (8, _('8 Days')),
    (9, _('9 Days')),
    (10, _('10 Days')),
    (11, _('11 Days')),
    (12, _('12 Days')),
    (13, _('13 Days')),
    (14, _('14 Days')),
)


class MailingList(models.Model):
    name = models.CharField(_('Name'), unique=True, max_length=128)
    full_content = models.BooleanField(
        _('Full Content'), default=False,
        help_text=_('Send full content of items'))
    private = models.BooleanField(_('Private'), default=False)
    last_sent = models.DateTimeField(_('Last Sent'), blank=True, null=True)
    send_days = models.IntegerField(_('Send every X days'),
                                    blank=True, null=True, default=0,
                                    choices=SEND_DAYS_CHOICES)
    send_count = models.IntegerField(
        _('Send every X items'), blank=True, null=True, default=0,
        help_text=_('0 Means no emails based on items count'))
    last_checked = models.DateTimeField(_('Last Checked'),
                                        blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    ctype = models.PositiveIntegerField(
        _('List for Content Type'), blank=True, null=True,
        choices=CONTENT_TYPE_CHOICES,
        help_text=_('Leave empty for all content types'))
    categories = models.ManyToManyField(
        ContentCategory, related_name='mailing_lists', verbose_name=_('Topics'),
        blank=True)

    subscribers = models.ManyToManyField(User, verbose_name=_('Subscribers'),
                                         related_name='mailing_lists')

    class Meta:
        verbose_name = _('Mailing List')
        verbose_name_plural = _('Mailing Lists')

    def __str__(self):
        return self.name

    def get_content_queryset(self, now=None, count=None):
        from_date = self.last_sent
        if now is None:
            if settings.USE_TZ:
                now = timezone.now()
            else:
                now = datetime.now()

        if not from_date:
            if self.send_days:
                from_date = now - timedelta(days=self.send_days)
            elif self.send_count:
                from_date = now - timedelta(days=360)

        if self.send_days and self.last_sent > now - timedelta(self.send_days):
            return CommonContent.objects.none()

        qs = CommonContent.objects.filter(published=True, language='he')

        if self.ctype:
            qs = qs.filter(ctype=self.ctype)

        if self.categories.exists():
            qs = qs.filter(categories__in=self.categories.all())

        if count is None:
            qs = qs.filter(created_at__gt=from_date)

        qs = qs.order_by('-created_at').distinct()

        if count is None:
            if self.send_count:
                qs = qs[:self.send_count]
        else:
            qs = qs[:count]

        return qs


class Subscriber(User):
    class Meta:
        proxy = True
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscribers')
