# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('color', colorfield.fields.ColorField(max_length=10, default='#FF0000', verbose_name='Color')),
                ('icon_css_class', models.CharField(blank=True, max_length=40, verbose_name='CSS icon class')),
                ('language', models.CharField(max_length=5, choices=[('he', 'Hebrew'), ('en', 'English')], db_index=True, verbose_name='Language')),
                ('is_hot', models.BooleanField(default=False, db_index=True, verbose_name='Hot Topic')),
                ('followers', models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Generic Categories',
                'verbose_name': 'Generic Category',
            },
        ),
    ]
