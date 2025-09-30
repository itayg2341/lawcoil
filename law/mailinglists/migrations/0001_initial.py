# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128, verbose_name='Name')),
                ('private', models.BooleanField(verbose_name='Private', default=False)),
                ('last_sent', models.DateTimeField(null=True, verbose_name='Last Sent', blank=True)),
                ('send_days', models.IntegerField(choices=[(0, 'Do not send by days'), (1, '1 Days'), (2, '2 Days'), (3, '3 Days'), (4, '4 Days'), (5, '5 Days'), (6, '6 Days'), (7, '7 Days'), (8, '8 Days'), (9, '9 Days'), (10, '10 Days'), (11, '11 Days'), (12, '12 Days'), (13, '13 Days'), (14, '14 Days')], null=True, verbose_name='Send every X days', blank=True, default=0)),
                ('send_count', models.IntegerField(null=True, verbose_name='Send every X items', blank=True, default=0)),
            ],
        ),
    ]
