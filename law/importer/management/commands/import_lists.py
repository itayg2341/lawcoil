from law.content.const import CONTENT_TYPE
from law.content.models import ContentCategory
from law.importer.management.base_import_command import BaseImportCommand
from law.importer.models import LegacyLists
from law.mailinglists.models import MailingList


class Command(BaseImportCommand):
    help = 'Import old mailing lists'

    TABLES = [m._meta.db_table for m in (MailingList.categories.through,
                                         MailingList)]

    def handle(self, *args, **options):
        self.stdout.write('Importing Lists')
        self.clear_tables()
        self.import_lists()
        self.reset_sequences()

    def clear_tables(self, cascade=False):
        MailingList.objects.all().delete()

    def import_lists(self):
        self.stdout.write('- Importing Mailing Lists')
        self.create_news_mailing_list()
        self.create_computer_law_mailing_list()
        self.create_privacy_mailing_list()
        self.create_intellectual_property_list()
        self.create_copyright_list()

    @staticmethod
    def fix_quotes(content):
        return content.replace('\\"', '"')

    def create_news_mailing_list(self):
        old_list = LegacyLists.objects.get(pk=1)
        self.stdout.write('  * ' + str(old_list))

        new_list = MailingList(
            name=old_list.name,
            private=old_list.private,
            last_sent=old_list.last_sent,
            last_checked=old_list.last_checked,
            send_count=old_list.send_count,
            send_days=old_list.send_days,
            description=self.fix_quotes(old_list.description),
            ctype=CONTENT_TYPE.news.value
        )

        new_list.save()

    def create_computer_law_mailing_list(self):
        old_list = LegacyLists.objects.get(pk=2)
        self.stdout.write('  * ' + str(old_list))

        new_list = MailingList(
            name=old_list.name,
            private=old_list.private,
            last_sent=old_list.last_sent,
            last_checked=old_list.last_checked,
            send_count=old_list.send_count,
            send_days=old_list.send_days,
            description=self.fix_quotes(old_list.description),
            ctype=CONTENT_TYPE.computer_law.value
        )

        new_list.save()

    def create_privacy_mailing_list(self):
        old_list = LegacyLists.objects.get(pk=8)
        self.stdout.write('  * ' + str(old_list))

        new_list = MailingList(
            name=old_list.name,
            private=old_list.private,
            last_sent=old_list.last_sent,
            last_checked=old_list.last_checked,
            send_count=old_list.send_count,
            send_days=old_list.send_days,
            description=self.fix_quotes(old_list.description),
            ctype=CONTENT_TYPE.news.value
        )

        new_list.save()

        slugs = ['privacy-security', 'spam-email']
        new_list.categories = ContentCategory.objects.filter(slug__in=slugs)

    def create_intellectual_property_list(self):
        old_list = LegacyLists.objects.get(pk=5)
        self.stdout.write('  * ' + str(old_list))

        new_list = MailingList(
            name=old_list.name,
            private=old_list.private,
            last_sent=old_list.last_sent,
            last_checked=old_list.last_checked,
            send_count=old_list.send_count,
            send_days=old_list.send_days,
            description=self.fix_quotes(old_list.description),
            ctype=CONTENT_TYPE.news.value
        )

        new_list.save()

        slugs = ['patents', 'domain-names', 'open-source', 'trademarks',
                 'copyright']
        new_list.categories = ContentCategory.objects.filter(slug__in=slugs)

    def create_copyright_list(self):
        old_list = LegacyLists.objects.get(pk=3)
        self.stdout.write('  * ' + str(old_list))

        new_list = MailingList(
            name=old_list.name,
            private=old_list.private,
            last_sent=old_list.last_sent,
            last_checked=old_list.last_checked,
            send_count=old_list.send_count,
            send_days=old_list.send_days,
            description=self.fix_quotes(old_list.description),
            ctype=CONTENT_TYPE.news.value
        )

        new_list.save()

        slugs = ['copyright']
        new_list.categories = ContentCategory.objects.filter(slug__in=slugs)
