# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151110_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='encryped_password',
            new_name='encrypted_password',
        ),
    ]
