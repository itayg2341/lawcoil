# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20160828_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharecontact',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='User', related_name='shared_contacts', on_delete=models.CASCADE),
        ),
    ]
