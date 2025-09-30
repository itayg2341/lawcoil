# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareContact',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('email', models.EmailField(verbose_name='Email', max_length=255)),
                ('user', models.ForeignKey(verbose_name='User', related_name='share_contacts', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Share Contact',
                'verbose_name_plural': 'Share Contacts',
            },
        ),
        migrations.AlterUniqueTogether(
            name='sharecontact',
            unique_together=set([('user', 'email')]),
        ),
    ]
