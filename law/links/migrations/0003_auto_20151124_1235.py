# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20151124_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='catdesc',
        ),
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
