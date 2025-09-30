from django.contrib import admin

from .models import Contributor


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):

    list_display = ('name', 'order', 'show_link', 'is_default')
    fields = ('name', 'link', 'show_link', 'lawyer', 'is_default', 'short_desc',
              'small_photo', 'order')
    ordering = ('order', 'name')
    search_fields = ('name', )
    list_filter = ('show_link', 'is_default')
    list_editable = ('order', )

    class Media:
        css = {
            'all': ('css/django_admin_rtl_fixes.css', )
        }
