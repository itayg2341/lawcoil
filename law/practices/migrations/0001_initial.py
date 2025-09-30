# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeArea',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200, verbose_name='Name')),
                ('language', models.CharField(choices=[('he', 'Hebrew'), ('en', 'English')], max_length=5, db_index=True, verbose_name='Language')),
                ('slug', models.SlugField(max_length=60, blank=True, verbose_name='Slug')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('published', models.BooleanField(default=True, db_index=True, verbose_name='Published')),
                ('order', models.IntegerField(default=1, db_index=True, verbose_name='Order')),
            ],
            options={
                'verbose_name_plural': 'Practice Areas',
                'ordering': ('order',),
                'verbose_name': 'Practice Area',
            },
        ),
    ]
