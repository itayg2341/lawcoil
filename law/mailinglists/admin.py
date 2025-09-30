from django.contrib import admin
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from .forms import SubscriberAdminForm
from .models import MailingList, Subscriber
from law.core.filters import RelatedDropdownFilter


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):

    list_display = ('name', 'full_content', 'last_sent', 'last_checked',
                    'send_days', 'send_count', 'private', 'ctype',
                    'categories_str')
    readonly_fields = ('last_sent', 'last_checked')
    filter_horizontal = ('categories', 'subscribers')

    class Media:
        css = {
            'all': ('css/django_admin_rtl_fixes.css', )
        }

    def categories_str(self, obj):
        obj_cats = obj.categories.values_list('name', flat=True)
        if not obj_cats:
            return _('All Categories')
        return ', '.join(obj_cats)
    categories_str.short_description = _('Categories')


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):

    form = SubscriberAdminForm
    fields = ('username', 'email', 'send_newsletters', 'first_name',
              'last_name', 'lists', 'watch_words')
    readonly_fields = ('username', 'email', 'first_name', 'last_name')
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'send_newsletters', 'user_lists')
    list_editable = ('send_newsletters', )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (
        'send_newsletters',
        ('mailing_lists', RelatedDropdownFilter),
    )

    class Media:
        css = {
            'all': ('css/django_admin_rtl_fixes.css', )
        }

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # qs = (qs.annotate(mailing_lists_count=Count('mailing_lists'))
        #         .filter(mailing_lists_count__gt=0)
        #         .prefetch_related('mailing_lists'))
        qs = qs.order_by('username').prefetch_related('mailing_lists')
        return qs

    def user_lists(self, obj):
        return ', '.join(str(m) for m in obj.mailing_lists.all())
    user_lists.short_description = _('Mailing Lists')
