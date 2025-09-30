# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NarrowPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(verbose_name='Photo', upload_to='wide_photos')),
            ],
            options={
                'verbose_name': 'Narrow Photo',
                'verbose_name_plural': 'Narrow Photos',
            },
        ),
        migrations.CreateModel(
            name='WidePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(verbose_name='Photo', upload_to='wide_photos')),
            ],
            options={
                'verbose_name': 'Wide Photo',
                'verbose_name_plural': 'Wide Photos',
            },
        ),
    ]
