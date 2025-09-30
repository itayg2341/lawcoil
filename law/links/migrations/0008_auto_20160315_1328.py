# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0007_auto_20160315_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='engname',
            field=models.CharField(max_length=200, blank=True, null=True, db_index=True, verbose_name='English name'),
        ),
        migrations.AlterField(
            model_name='link',
            name='hebname',
            field=models.CharField(max_length=200, blank=True, null=True, db_index=True, verbose_name='Hebrew name'),
        ),
        migrations.AlterField(
            model_name='link',
            name='online',
            field=models.BooleanField(default=True, db_index=True, verbose_name='Online'),
        ),
    ]
