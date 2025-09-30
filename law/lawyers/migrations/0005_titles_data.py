# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

TITLES = {
    'haim-ravia': {
        'he': 'שותף בכיר, יו"ר קבוצת קבוצת האינטרנט, הסייבר וזכויות היוצרים',
        'en': 'Senior Partner, Chair of the Internet, Cyber & Copyright Group',
    },
    'tal-kaplan': {
        'he': 'שותף',
        'en': 'Partner',
    },
    'dotan-hammer': {
       'he': 'שותף בכיר',
       'en': 'Senior Associate',
    },
}

def add_lawyers_titles(apps, schema_editor):
    Lawyer = apps.get_model('lawyers', 'Lawyer')

    for slug, titles in TITLES.items():
        for lang, title in titles.items():
            lawyer = Lawyer.objects.get(slug=slug, language=lang)
            lawyer.title = title
            lawyer.save()


def remove_lawyers_titles(apps, schema_editor):
    Lawyer = apps.get_model('lawyers', 'Lawyer')
    Lawyer.objects.filter(slug__in=TITLES.keys()).update(title=None)


class Migration(migrations.Migration):

    dependencies = [
        ('lawyers', '0004_lawyer_title'),
    ]

    operations = [
        migrations.RunPython(add_lawyers_titles,
                             reverse_code=remove_lawyers_titles)
    ]
