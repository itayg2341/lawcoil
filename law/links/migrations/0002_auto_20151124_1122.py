# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engname', models.CharField(max_length=200, verbose_name='English name')),
                ('hebname', models.CharField(max_length=200, verbose_name='Hebrew name')),
                ('url', models.URLField(blank=True, null=True, max_length=255, verbose_name='URL')),
                ('engdesc', models.TextField(blank=True, null=True, verbose_name='English description')),
                ('hebdesc', models.TextField(blank=True, null=True, verbose_name='Hebrew description')),
                ('created_at', models.DateField(blank=True, db_index=True, null=True, default=django.utils.timezone.now, verbose_name='Created at')),
                ('online', models.BooleanField(default=True, verbose_name='Online')),
            ],
            options={
                'verbose_name_plural': 'Links',
                'verbose_name': 'Link',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, verbose_name='parent', related_name='children', to='links.Category', null=True, on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='links',
            name='categories',
            field=models.ManyToManyField(related_name='links', to='links.Category', verbose_name='Categories'),
        ),
    ]
