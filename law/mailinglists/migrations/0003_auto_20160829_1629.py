# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20160821_1506'),
        ('mailinglists', '0002_auto_20160829_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailinglist',
            name='categories',
            field=models.ManyToManyField(verbose_name='Topics', related_name='mailing_lists', to='content.ContentCategory'),
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='send_count',
            field=models.IntegerField(default=0, verbose_name='Send every X items', null=True, help_text='0 Means no emails based on items count', blank=True),
        ),
    ]
