# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_auto_20151124_1235'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
    ]
