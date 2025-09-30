from django.contrib import admin
from .models import Page


@admin.register(Page)
class PagesAdmin(admin.ModelAdmin):

    search_fields = ('title', 'content')
    list_display = ('title', 'slug', 'language')

    class Media:
        css = {
           'all': ('css/django_admin_rtl_fixes.css', )
        }
        js = ('js/admin_adjust.js', )
