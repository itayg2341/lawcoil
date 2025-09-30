# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('language', models.CharField(verbose_name='Language', db_index=True, choices=[('he', 'Hebrew'), ('en', 'English')], max_length=5)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('slug', models.SlugField(verbose_name='Slug', max_length=60)),
                ('email', models.EmailField(verbose_name='Email', max_length=254)),
                ('phone', models.CharField(verbose_name='Phone', max_length=100)),
                ('short_description', ckeditor.fields.RichTextField(verbose_name='Short Description')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('profile_photo', easy_thumbnails.fields.ThumbnailerImageField(verbose_name='Small Profile Photo', upload_to='lawyers')),
                ('large_photo', models.ImageField(verbose_name='Large Photo', upload_to='lawyers')),
                ('order', models.IntegerField(verbose_name='Order', default=0, db_index=True)),
            ],
            options={
                'verbose_name': 'Lawyer',
                'verbose_name_plural': 'Group Lawyers',
            },
        ),
    ]
