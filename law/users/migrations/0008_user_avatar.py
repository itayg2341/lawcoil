# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160825_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, verbose_name='Avatar', upload_to='avatars'),
        ),
    ]
