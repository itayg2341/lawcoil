# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0005_auto_20160315_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='categories',
            field=mptt.fields.TreeManyToManyField(related_name='links', to='links.Category', verbose_name='Categories'),
        ),
    ]
