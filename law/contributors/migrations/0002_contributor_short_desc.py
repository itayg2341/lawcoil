# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='short_desc',
            field=models.TextField(blank=True, null=True, verbose_name='Short Description'),
        ),
    ]
