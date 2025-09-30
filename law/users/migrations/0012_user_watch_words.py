# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20160828_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watch_words',
            field=models.TextField(verbose_name='Watch words', blank=True, null=True),
        ),
    ]
