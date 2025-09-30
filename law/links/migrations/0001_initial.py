# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('lang', models.CharField(choices=[('he', 'Hebrew'), ('en', 'English')], verbose_name='Language', max_length=10, db_index=True)),
                ('name', models.CharField(unique=True, verbose_name='Name', max_length=128)),
                ('catdesc', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(null=True, to='links.Category', related_name='children', blank=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Links category',
                'verbose_name_plural': 'Links categories',
            },
        ),
    ]
