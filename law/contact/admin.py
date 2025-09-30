from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import FeedbackMessage


@admin.register(FeedbackMessage)
class FeedbackMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'formatted_email', 'received_at')
    search_fields = ('name', 'email', 'message')
    fields = ('name', 'formatted_email', 'phone', 'role',
              'organization', 'content', 'received_at')
    readonly_fields = ('name', 'formatted_email', 'phone', 'role',
                       'organization', 'content', 'received_at')
    date_hierarchy = 'received_at'

    def has_add_permission(self, request):
        return False

    def formatted_email(self, obj):
        return format_html('<a href="mailto:{}">{}</a>', obj.email, obj.email)
    formatted_email.admin_order_field = 'email'
    formatted_email.short_description = _('Email')
