# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0004_commoncontent_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Articles',
                'ordering': ['-created_at'],
                'verbose_name': 'Article',
                'proxy': True,
            },
            bases=('content.commoncontent',),
        ),
        migrations.CreateModel(
            name='ComputerLaw',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Computer Laws',
                'ordering': ['-created_at'],
                'verbose_name': 'Computer Law',
                'proxy': True,
            },
            bases=('content.commoncontent',),
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
            ],
            options={
                'verbose_name_plural': 'News Items',
                'ordering': ['-created_at'],
                'verbose_name': 'News Item',
                'proxy': True,
            },
            bases=('content.commoncontent',),
        ),
        migrations.AlterModelOptions(
            name='contentcategory',
            options={'verbose_name': 'Content Category', 'verbose_name_plural': 'Content Categories'},
        ),
        migrations.AddField(
            model_name='commoncontent',
            name='saved_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='items'),
        ),
    ]
