from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

from .models import WidePhoto, NarrowPhoto


class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" style="max-height: 100px"/></a>' % \
                (image_url, image_url, file_name))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


@admin.register(WidePhoto)
class WidePhotoAdmin(admin.ModelAdmin):

    list_display = ('photo_img', '__str__')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'photo':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super().formfield_for_dbfield(db_field, **kwargs)


@admin.register(NarrowPhoto)
class NarrowPhotoAdmin(WidePhotoAdmin):
    pass

