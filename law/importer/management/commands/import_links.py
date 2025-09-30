from django.core.management.base import CommandError
from law.importer.management.base_import_command import BaseImportCommand

from law.importer.models import LegacyLinkscat, LegacyLinks
from law.links.models import Category, Link


class Command(BaseImportCommand):
    help = 'Import old links and categories'

    TABLES = [m._meta.db_table for m in (Link.categories.through, Category,
                                         Link)]

    def handle(self, *args, **options):
        self.stdout.write('Importing Links')
        self.clear_tables()
        self.import_categories()
        self.import_links()
        self.reset_sequences()

    def import_categories(self):
        self.stdout.write('- Importing categories')
        LANGUAGES = {'h': 'he', 'e': 'en'}

        for cat in LegacyLinkscat.objects.order_by('pk'):
            self.stdout.write('  * ' + str(cat))
            try:
                new_cat = Category(lang=LANGUAGES[cat.lang],
                                   name=cat.name,
                                   desc=cat.catdesc,
                                   slug=cat.slug)
                new_cat.pk = cat.pk
                new_cat.save()
            except KeyError:
                raise CommandError('Unknown language "%s"' % cat.lang)

        self.stdout.write('- Setting categories parents')
        for cat in LegacyLinkscat.objects.order_by('pk'):
            self.stdout.write('  * ' + str(cat))
            if cat.parent:
                new_cat = Category.objects.get(pk=cat.pk)
                new_cat.parent = Category.objects.get(pk=cat.parent.pk)
                new_cat.save()

    def import_links(self):
        self.stdout.write('- Importing links')

        for link in LegacyLinks.objects.all():
            self.stdout.write('  * ' + str(link))
            engname = link.engname.replace('&quot;', '"').replace('&quot', '"')
            engname = engname.replace('&amp;', '&')
            hebname = link.hebname.replace('&quot;', '"').replace('&quot', '"')
            hebname = hebname.replace('&amp;', '&')
            new_link = Link(engname=engname, hebname=hebname,
                            url=link.url, engdesc=link.engdesc,
                            hebdesc=link.hebdesc, created_at=link.date,
                            online=link.offline != 'y')
            new_link.save()
            new_link.categories = [Category.objects.get(pk=x.pk) for x in
                                   link.categories.all()]
