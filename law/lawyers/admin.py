from django.contrib import admin

from .models import Lawyer


@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'slug', 'order')
    list_filter = ('language', )
    search_fields = ('name', 'slug')
    list_editable = ('order', )
