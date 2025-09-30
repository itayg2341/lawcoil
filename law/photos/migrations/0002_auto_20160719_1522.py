# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narrowphoto',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='narrow_photos', verbose_name='Photo'),
        ),
    ]
