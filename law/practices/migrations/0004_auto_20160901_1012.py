# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practices', '0003_auto_20160901_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicearea',
            name='slug',
            field=models.SlugField(verbose_name='Slug', max_length=60),
        ),
        migrations.AlterField(
            model_name='practicearea',
            name='title',
            field=models.CharField(verbose_name='Title', max_length=200),
        ),
    ]
