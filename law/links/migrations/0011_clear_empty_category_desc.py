# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def clear_empty_desc(apps, schema_editor):
    Category = apps.get_model('links', 'Category')

    Category.objects.filter(desc='<br type="_moz" />').update(desc=None)


def dummy(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0010_auto_20160315_1341'),
    ]

    operations = [
        migrations.RunPython(clear_empty_desc, dummy)
    ]
