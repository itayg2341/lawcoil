# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160809_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='saveditem',
            name='language',
            field=models.CharField(max_length=5, db_index=True, choices=[('he', 'Hebrew'), ('en', 'English')], default='he', verbose_name='Language'),
            preserve_default=False,
        ),
    ]
