# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('is_default', models.BooleanField(default=False, verbose_name='Default ?')),
            ],
            options={
                'verbose_name': 'Contributor',
                'verbose_name_plural': 'Contributors',
            },
        ),
    ]
