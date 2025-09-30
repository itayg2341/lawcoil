# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0006_auto_20160315_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='engname',
            field=models.CharField(null=True, max_length=200, verbose_name='English name', blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='hebname',
            field=models.CharField(null=True, max_length=200, verbose_name='Hebrew name', blank=True),
        ),
    ]
