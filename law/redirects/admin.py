from django.contrib import admin

from .models import Redirects


@admin.register(Redirects)
class RedirectsAdmin(admin.ModelAdmin):
    search_fields = ('from_url', 'to_url', 'comment')
    list_display = ('from_url', 'to_url', 'comment')

    class Media:
        css = {
           'all': ('css/django_admin_rtl_fixes.css', )
        }
        js = ('js/admin_adjust.js', )
