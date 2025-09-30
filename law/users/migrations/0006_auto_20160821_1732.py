# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_saveditem_language'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='saveditem',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='saveditem',
            name='item_ct',
        ),
        migrations.RemoveField(
            model_name='saveditem',
            name='user',
        ),
        migrations.DeleteModel(
            name='SavedItem',
        ),
    ]
