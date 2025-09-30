# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailinglists', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailinglist',
            options={'verbose_name_plural': 'Mailing Lists', 'verbose_name': 'Mailing List'},
        ),
        migrations.AddField(
            model_name='mailinglist',
            name='description',
            field=models.TextField(null=True, blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='mailinglist',
            name='last_checked',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Last Checked'),
        ),
    ]
