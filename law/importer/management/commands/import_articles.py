from datetime import datetime

import pytz
from django.utils import timezone

from law.content.const import CONTENT_TYPE
from law.content.models import ContentCategory, CommonContent
from law.contributors.models import Contributor
from law.importer.category_mappings import CATEGORIES_SLUGS_MAP
from law.importer.management.base_import_command import BaseImportCommand
from law.importer.models import LegacyArticles, LegacyArticlescat


ARTICLES_PKS = [1, 21]


class Command(BaseImportCommand):
    help = 'Import old articles'

    TABLES = [m._meta.db_table for m in (CommonContent,)]

    def handle(self, *args, **options):

        self.stdout.write('Importing Articles')
        self.clear_tables()
        self.import_articles()
        self.reset_sequences()

    def clear_tables(self, cascade=False):
        CommonContent.objects.filter(ctype=CONTENT_TYPE.articles.value).delete()

    def import_articles(self):
        no_slug_counter = 1

        root_cats = list(LegacyArticlescat.objects.filter(pk__in=ARTICLES_PKS))
        art_cats = list(LegacyArticlescat.objects.filter(parent__in=root_cats))

        qs = LegacyArticles.objects.filter(
            categories__in=art_cats + root_cats).distinct()
        qs = qs.order_by('date')
        for n in qs:
            self.stdout.write('* ' + str(n) + ' [' + n.lang + ']')

            slug = n.slug

            # ensure we have a slug
            if not slug:
                slug = 'default-slug-%d' % no_slug_counter
                no_slug_counter += 1

            try:
                as_datetime = datetime.combine(n.date, datetime.min.time())

                created_at = timezone.make_aware(
                    as_datetime, timezone=pytz.timezone('Israel'))
            except (pytz.NonExistentTimeError, pytz.AmbiguousTimeError):
                tz = pytz.timezone('Israel')
                created_at = tz.localize(
                    datetime.fromtimestamp(as_datetime.timestamp()),
                    is_dst=False)

            item = CommonContent(
                title=n.title,
                slug=slug,
                ctype=CONTENT_TYPE.articles.value,
                created_at=created_at,
                content=n.data,
                language='en' if n.lang == 'e' else 'he',
                published=n.offline != 'y',
                sub_title=n.subtitle,
                short_desc=n.shortdesc,
                email_notified=True
            )
            item.save()

            contributor_name = n.contributed.replace('&quot;', '"')
            contributor, _ = Contributor.objects.get_or_create(
                name=contributor_name)

            item.contributors = [contributor]

            if n.lang == 'h':
                categories = self._get_categories(n, art_cats)
            else:
                categories = ContentCategory.objects.filter(language='en')

            item.categories = categories

    @staticmethod
    def _get_categories(orig_item, art_cats):
        cats_pks = set([x.pk for x in art_cats])
        return [ContentCategory.objects.get(slug=CATEGORIES_SLUGS_MAP[x.slug])
                for x in orig_item.categories.filter(pk__in=cats_pks)]
