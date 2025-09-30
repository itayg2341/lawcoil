from django.utils import timezone

from law.content.const import CONTENT_TYPE
from law.content.models import ContentCategory, CommonContent
from law.contributors.models import Contributor
from law.importer.category_mappings import CATEGORIES_SLUGS_MAP
from law.importer.management.base_import_command import BaseImportCommand
from law.importer.models import LegacyNews, LegacyNewscat

NEWS_PKS = [7, 51]


class Command(BaseImportCommand):
    help = 'Import old news items'

    TABLES = [m._meta.db_table for m in (CommonContent,)]

    def handle(self, *args, **options):

        self.stdout.write('Importing News Items')
        self.clear_tables()
        self.import_news()
        self.reset_sequences()

    def clear_tables(self, cascade=False):
        CommonContent.objects.filter(ctype=CONTENT_TYPE.news.value).delete()

    def import_news(self):
        no_slug_counter = 1

        root_cats = list(LegacyNewscat.objects.filter(pk__in=NEWS_PKS))
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

            news_item = CommonContent(
                title=n.title,
                slug=slug,
                ctype=CONTENT_TYPE.news.value,
                created_at=n.date or timezone.now(),
                content=n.data,
                language='en' if n.lang == 'e' else 'he',
                published=n.offline != 'y',
                email_notified=True
            )
            news_item.save()

            contributor_name = n.contributed.replace('&quot;', '"')
            contributor = Contributor.objects.get(name=contributor_name)

            news_item.contributors = [contributor]

            if n.lang == 'h':
                categories = self._get_news_categories(n, news_cats)
            else:
                categories = ContentCategory.objects.filter(language='en')

            news_item.categories = categories

    @staticmethod
    def _get_news_categories(orig_news_item, news_cats):
        """docstring for _get_news_categories"""
        news_cats_pks = set([x.pk for x in news_cats])
        return [ContentCategory.objects.get(slug=CATEGORIES_SLUGS_MAP[x.slug])
                for x in orig_news_item.categories.filter(pk__in=news_cats_pks)]
