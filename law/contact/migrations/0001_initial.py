# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=200)),
                ('email', models.EmailField(verbose_name='Email', max_length=250)),
                ('phone', models.CharField(verbose_name='Phone', blank=True, null=True, max_length=40)),
                ('role', models.CharField(verbose_name='Role', blank=True, null=True, max_length=100)),
                ('organization', models.CharField(verbose_name='Organization', blank=True, null=True, max_length=200)),
                ('content', models.TextField(verbose_name='Content')),
                ('received_at', models.DateTimeField(verbose_name='Received At', auto_now_add=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Feedback Message',
                'ordering': ('received_at',),
                'verbose_name_plural': 'Feedback Messages',
            },
        ),
    ]
