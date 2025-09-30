from django.contrib import admin
from django.db.models import Count
from django.utils.translation import gettext_lazy as _


class ListSubscriberFilter(admin.SimpleListFilter):
    """Enable filtering by users subscribed to mailing lists"""

    title = _('Mailing List Subsctiber')
    parameter_name = 'is_subscriber'

    def lookups(self, request, model_admin):
        return (
            ('1', _('Yes')),
            ('0', _('No')),
        )

    def queryset(self, request, queryset):

        if self.value() == '0':
            return (queryset.annotate(lists_count=Count('mailing_lists'))
                    .filter(lists_count=0))
        if self.value() == '1':
            return (queryset.annotate(lists_count=Count('mailing_lists'))
                    .filter(lists_count__gt=0))

