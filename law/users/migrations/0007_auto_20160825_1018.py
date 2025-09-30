# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160821_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(verbose_name='Address', blank=True, null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.CharField(verbose_name='Organization', blank=True, null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(verbose_name='Phone', blank=True, null=True, max_length=40),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(verbose_name='Role', blank=True, null=True, max_length=100),
        ),
    ]
