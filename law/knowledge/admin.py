from django.contrib import admin

from .models import KnowledgeCenter, KnowledgeCenterItem


@admin.register(KnowledgeCenter)
class KnowledgeAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug', 'order')
    list_editable = ('order', )
    search_fields = ('name', 'description')

    class Media:
        css = {
            'all': ('css/django_admin_rtl_fixes.css', )
        }
        js = ('js/admin_adjust.js', )


@admin.register(KnowledgeCenterItem)
class KnowledgeCenterItemAdmin(admin.ModelAdmin):

    raw_id_fields = ('article', 'news_item', 'computer_law')
    list_select_related = ('knowledge_center', )
    list_display = ('computed_title', 'knowledge_center', 'slug', 'order',
                    'display_in_listing', 'type_description')
    list_filter = ('knowledge_center', )
    list_editable = ('order', 'display_in_listing')
    ordering = ('knowledge_center', 'order')

    class Media:
        css = {
            'all': ('css/django_admin_rtl_fixes.css', )
        }
        js = ('js/admin_adjust.js', )
