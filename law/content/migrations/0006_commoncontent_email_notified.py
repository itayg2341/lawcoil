# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20160821_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='commoncontent',
            name='email_notified',
            field=models.BooleanField(verbose_name='Email words notification sent', default=False),
        ),
    ]
