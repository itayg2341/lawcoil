# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0003_contributor_small_photo'),
        ('content', '0002_categories_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonContent',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=196, verbose_name='Title')),
                ('slug', models.SlugField(max_length=60, blank=True, verbose_name='Slug')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True, verbose_name='Created At')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('language', models.CharField(max_length=5, choices=[('he', 'Hebrew'), ('en', 'English')], db_index=True, verbose_name='Language')),
                ('published', models.BooleanField(default=True, db_index=True, verbose_name='Published')),
                ('ctype', models.PositiveIntegerField(choices=[(1, 'articles'), (2, 'news'), (3, 'computer_law')], verbose_name='Content Type')),
                ('reading_time', models.IntegerField(blank=True, verbose_name='Reading Time')),
                ('sub_title', models.CharField(null=True, max_length=255, blank=True, verbose_name='Sub Title')),
                ('short_desc', ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Short Description')),
                ('attachment', models.FileField(null=True, max_length=255, blank=True, upload_to='computer-law', verbose_name='Attached file')),
                ('url', models.URLField(null=True, blank=True, verbose_name='Link to')),
                ('contributors', models.ManyToManyField(related_name='commoncontent', to='contributors.Contributor', verbose_name='Contributors')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterIndexTogether(
            name='commoncontent',
            index_together=set([('language', 'ctype', 'created_at')]),
        ),
    ]
