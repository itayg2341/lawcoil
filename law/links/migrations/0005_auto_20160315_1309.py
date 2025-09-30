# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0004_auto_20151124_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='engdesc',
            field=ckeditor.fields.RichTextField(verbose_name='English description', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='hebdesc',
            field=ckeditor.fields.RichTextField(verbose_name='Hebrew description', null=True, blank=True),
        ),
    ]
