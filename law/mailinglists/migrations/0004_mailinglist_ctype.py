# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailinglists', '0003_auto_20160829_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailinglist',
            name='ctype',
            field=models.PositiveIntegerField(verbose_name='List for Content Type', blank=True, null=True, choices=[(1, 'articles'), (2, 'news'), (3, 'computer_law')]),
        ),
    ]
