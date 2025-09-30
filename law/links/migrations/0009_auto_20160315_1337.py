# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0008_auto_20160315_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(to='links.Category', related_name='children', verbose_name='Parent', blank=True, null=True, on_delete=models.CASCADE),
        ),
    ]
