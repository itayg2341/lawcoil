# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0009_auto_20160315_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=ckeditor.fields.RichTextField(verbose_name='Description', null=True, blank=True),
        ),
    ]
