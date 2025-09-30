from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Link
from law.core.filters import TreeDropdownFilter


@admin.register(Category)
class LinksCategoryAdmin(MPTTModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('lang',)

    class Media:
        css = {
            'all': ('css/django_admin_rtl_fixes.css', )
        }
        js = ('js/admin_adjust.js', )


@admin.register(Link)
class LinksAdmin(admin.ModelAdmin):
    search_fields = ('engname', 'hebname')
    list_display = ('hebname', 'engname', 'online')
    list_display_links = ('engname', 'hebname')
    list_filter = (
        'online',
        ('categories', TreeDropdownFilter),
    )
    date_hierarchy = 'created_at'

    class Media:
        css = {
            'all': ('css/django_admin_rtl_fixes.css', )
        }
        js = ('js/admin_adjust.js', )
