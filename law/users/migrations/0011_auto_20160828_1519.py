# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20160828_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharecontact',
            name='user',
            field=models.ForeignKey(verbose_name='User', related_name='share_contacts', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
        ),
    ]
