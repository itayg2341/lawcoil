# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20160817_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='commoncontent',
            name='categories',
            field=models.ManyToManyField(to='content.ContentCategory', verbose_name='Categories', related_name='items'),
        ),
    ]
