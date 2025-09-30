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

LEGISLATION_PKS = [24]


class Command(BaseImportCommand):
    help = 'Import old legislation'

    TABLES = [m._meta.db_table for m in (CommonContent,)]

    def handle(self, *args, **options):

        self.stdout.write('Importing Legislation')
        self.clear_tables()
        self.import_news()
        self.reset_sequences()

    def clear_tables(self, cascade=False):
        CommonContent.objects.filter(
            ctype=CONTENT_TYPE.legislation.value).delete()

    def import_news(self):
        no_slug_counter = 1

        root_cats = list(LegacyNewscat.objects.filter(pk__in=LEGISLATION_PKS))
        news_cats = list(LegacyNewscat.objects.filter(parent__in=root_cats))
        sub_cats = list(LegacyNewscat.objects.filter(parent__in=news_cats))

        all_cats = set(root_cats + news_cats + sub_cats)

        for n in LegacyNews.objects.filter(categories__in=all_cats).distinct():
            self.stdout.write('* ' + str(n) + ' [' + n.lang + ']')

            slug = n.slug

            # ensure we have a slug
            if not slug:
                slug = 'default-slug-%d' % no_slug_counter
                no_slug_counter += 1

            title = n.title

            news_item = CommonContent(
                title=title,
                slug=slug,
                ctype=CONTENT_TYPE.legislation.value,
                created_at=n.date or timezone.now(),
                content=n.data,
                language='en' if n.lang == 'e' else 'he',
                published=n.offline != 'y',
                email_notified=True
            )

            if '<a' in title:
                soup = BeautifulSoup(title, 'html.parser')
                link = soup.find('a')

                if link is not None:
                    title = strip_tags(title)
                    title = title.replace('&quot;', '"')
                    title = title.replace('&quot', '"')

                    news_item.title = title
                    attachment = link.attrs.get('href')

                    if attachment.startswith('/computer-law'):
                        attachment = '/media' + attachment

                    if attachment.startswith('/media'):
                        url = settings.OLD_LAW_CO_IL + attachment
                        try:
                            response = urlopen(url)
                            data = io.BytesIO(response.read())
                            filename = basename(attachment)
                            news_item.attachment.save(filename, File(data))
                        except HTTPError:
                            pass
                    else:
                        news_item.url = attachment

            news_item.save()

            contributor_name = n.contributed.replace('&quot;', '"')
            contributor = Contributor.objects.get(name=contributor_name)

            news_item.contributors = [contributor]

            if n.lang == 'h':
                categories = self._get_news_categories(n, sub_cats)
            else:
                categories = ContentCategory.objects.filter(language='en')

            news_item.categories = categories

    @staticmethod
    def _get_news_categories(orig_news_item, news_cats):
        """docstring for _get_news_categories"""
        news_cats_pks = set([x.pk for x in news_cats])
        cats = [ContentCategory.objects.get(slug=CATEGORIES_SLUGS_MAP[x.slug])
                for x in orig_news_item.categories.filter(pk__in=news_cats_pks)]
        if not cats:
            cats = [ContentCategory.objects.get(slug='regulation-government')]

        return list(set(cats))
