# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('users', '0003_auto_20160223_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('item_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(db_index=True)),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
                ('item_ct', models.ForeignKey(to='contenttypes.ContentType', on_delete=models.CASCADE)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name_plural': 'Saved Items',
                'verbose_name': 'Saved Item',
            },
        ),
        migrations.AlterUniqueTogether(
            name='saveditem',
            unique_together=set([('user', 'item_ct', 'item_id')]),
        ),
    ]
