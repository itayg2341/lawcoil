# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=196, verbose_name='Title')),
                ('slug', models.SlugField(max_length=60, verbose_name='Slug')),
                ('language', models.CharField(max_length=5, choices=[('he', 'Hebrew'), ('en', 'English')], db_index=True, verbose_name='Language')),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'verbose_name_plural': 'Pages',
                'verbose_name': 'Page',
            },
        ),
    ]
