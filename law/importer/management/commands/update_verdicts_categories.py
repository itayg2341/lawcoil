import io
from os.path import basename
from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup
from django.conf import settings
from django.core.files import File
from django.utils import timezone
from django.utils.html import strip_tags

from law.content.const import CONTENT_TYPE
from law.content.models import ContentCategory, CommonContent
from law.contributors.models import Contributor
from law.importer.category_mappings import CATEGORIES_SLUGS_MAP
from law.importer.management.base_import_command import BaseImportCommand
from law.importer.models import LegacyNews, LegacyNewscat

VERDICTS_PKS = [18]


class Command(BaseImportCommand):
    help = 'Update old verdicts'

    TABLES = [m._meta.db_table for m in (CommonContent,)]

    def handle(self, *args, **options):

        self.stdout.write('Importing Verdicts')
        self.update_categories()

    def update_categories(self):
        no_slug_counter = 1

        root_cats = list(LegacyNewscat.objects.filter(pk__in=VERDICTS_PKS))
        news_cats = list(LegacyNewscat.objects.filter(parent__in=root_cats))
        sub_cats = list(LegacyNewscat.objects.filter(parent__in=news_cats))

        all_cats = set(root_cats + news_cats + sub_cats)
        without_roots = set(news_cats + sub_cats)

        verdicts = LegacyNews.objects.filter(
            categories__in=all_cats).distinct()

        for n in verdicts:
            self.stdout.write('* ' + str(n) + ' [' + n.lang + ']')

            title = n.title
            if '<a' in title:
                soup = BeautifulSoup(title, 'html.parser')
                link = soup.find('a')

                if link is not None:
                    title = strip_tags(title)
                    title = title.replace('&quot;', '"')
                    title = title.replace('&quot', '"')


            try:
                news_item = CommonContent.objects.get(
                    title=title, ctype=CONTENT_TYPE.computer_law.value)
                self.stdout.write('  - found %s' % news_item)
            except CommonContent.DoesNotExist:
                self.stdout.write('  - not found %s, skipping' % title)
                continue
            except CommonContent.MultipleObjectsReturned:
                self.stdout.write('  - more than 1 found, taking 1st')
                news_item = CommonContent.objects.filter(
                    title=title, ctype=CONTENT_TYPE.computer_law.value).first()
                self.stdout.write('  - found %s' % news_item)

            if n.lang == 'h':
                categories = self._get_news_categories(n, without_roots)
            else:
                categories = ContentCategory.objects.filter(language='en')

            self.stdout.write('  - Setting categories to %s' % categories)
            news_item.categories = categories

    @staticmethod
    def _get_news_categories(orig_news_item, news_cats):
        """docstring for _get_news_categories"""
        news_cats_pks = set([x.pk for x in news_cats])

        cats = [ContentCategory.objects.get(slug=CATEGORIES_SLUGS_MAP[x.slug])
                for x in orig_news_item.categories.filter(pk__in=news_cats_pks)]
        if not cats:
            cats = [ContentCategory.objects.get(slug='misc')]

        return list(set(cats))
