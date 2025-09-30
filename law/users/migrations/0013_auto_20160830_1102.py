# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_user_watch_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='watch_words',
            field=models.TextField(verbose_name='Watch words', blank=True, help_text='Receive an email when a published article or news item contains a word or expression. Each word or expression in a separate line, minimum length is 4 characters.', max_length=300, null=True),
        ),
    ]
