# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailinglists', '0004_mailinglist_ctype'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailinglist',
            name='subscribers',
            field=models.ManyToManyField(related_name='mailing_lists', verbose_name='Subscribers', to=settings.AUTH_USER_MODEL),
        ),
    ]
