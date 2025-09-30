from django.contrib import admin

from .models import PracticeArea


@admin.register(PracticeArea)
class PracticeAreaAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'language', 'published', 'order')
    search_fields = ('title', 'slug', 'content')
    list_filter = ('language', 'published')
    list_editable = ('order', )

    class Media:
        css = {
            'all': ('css/django_admin_rtl_fixes.css', )
        }
        js = ('js/admin_adjust.js', )
