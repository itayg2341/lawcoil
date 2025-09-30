# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyers', '0002_lawyers_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lawyer',
            options={'verbose_name': 'Lawyer', 'verbose_name_plural': 'Group Lawyers', 'ordering': ('language', 'order')},
        ),
    ]
