# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyers', '0003_auto_20160831_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='title',
            field=models.CharField(verbose_name='Title', null=True, max_length=200, blank=True),
        ),
    ]
