# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practices', '0002_practices_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='practicearea',
            options={'verbose_name_plural': 'Practice Areas', 'verbose_name': 'Practice Area', 'ordering': ('language', 'order')},
        ),
    ]
