from law.importer.management.base_import_command import BaseImportCommand

from law.importer.models import LegacyContribs, LegacyNews
from law.contributors.models import Contributor


class Command(BaseImportCommand):
    help = 'Import Contributors'

    TABLES = [m._meta.db_table for m in (Contributor,)]

    def handle(self, *args, **options):

        self.stdout.write('Importing Contributors')
        self.clear_tables(cascade=True)
        self.import_contributors()
        self.import_contributors_from_news()
        self.reset_sequences()

    def import_contributors(self):
        for c in LegacyContribs.objects.order_by('pk'):
            self.stdout.write('* ' + str(c))

            new_conributor = Contributor(
                name=c.name,
                is_default=c.def_field == 'y'
            )
            new_conributor.save()

    def import_contributors_from_news(self):
        "Ensure we have all contributors"

        for c in LegacyNews.objects.values_list('contributed',
                                                flat=True).distinct():
            c = c.replace('&quot;', '"')
            _, created = Contributor.objects.get_or_create(name=c)

            if created:
                self.stdout.write('* From news:' + c)
