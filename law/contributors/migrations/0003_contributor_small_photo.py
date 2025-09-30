# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0002_contributor_short_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='small_photo',
            field=models.ImageField(verbose_name='Small Photo', null=True, blank=True, upload_to='contributors/', help_text='Small photo (125x125)'),
        ),
    ]
