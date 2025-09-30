from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils.translation import override

from law.content.mixins import ItemsGetterMixin
from law.lawyers.models import Lawyer
from law.links.models import Category
from law.practices.models import PracticeArea


class GenericItem:
    "Holds a static page or categproes landing page"

    def __init__(self, name, language, **url_kwargs):
        self.name = name
        self.language = language
        self.url_kwargs = url_kwargs

    def get_absolute_url(self):
        with override(self.language):
            return reverse(self.name, kwargs=self.url_kwargs)


class PagesSitemap(Sitemap):
    """General sitemap of the pages"""

    ENTRIES = [
        # he entries
        GenericItem('home', 'he'),
        GenericItem('content:index', 'he', content_type='news'),
        GenericItem('content:index', 'he', content_type='articles'),
        GenericItem('content:index', 'he', content_type='computer-law'),
        GenericItem('content:index', 'he', content_type='legislation'),
        GenericItem('links:index', 'he'),
        GenericItem('pages:page', 'he', slug='updates'),
        GenericItem('pages:page', 'he', slug='about'),
        GenericItem('pages:page', 'he', slug='about-group'),
        ('get_practices', 'he'),
        ('get_lawyers', 'he'),
        GenericItem('pages:page', 'he', slug='terms'),
        GenericItem('pages:page', 'he', slug='privacy'),
        GenericItem('contact:index', 'he'),

        # en entries
        GenericItem('home', 'en'),
        GenericItem('content:index', 'en', content_type='news'),
        GenericItem('content:index', 'en', content_type='articles'),
        GenericItem('pages:page', 'en', slug='about'),
        GenericItem('pages:page', 'en', slug='about-group'),
        GenericItem('links:index', 'en'),
        ('get_practices', 'en'),
        ('get_lawyers', 'en'),
        GenericItem('pages:page', 'en', slug='terms'),
        GenericItem('pages:page', 'en', slug='privacy'),
        GenericItem('contact:index', 'en'),
    ]

    def items(self):
        entries = []
        for entry in self.ENTRIES:
            if isinstance(entry, GenericItem):
                entries.append(entry)
            else:
                method, language = entry
                entries.extend(getattr(self, method)(language))
        return entries

    def get_practices(self, language):
        return PracticeArea.objects.filter(
            language=language, published=True).order_by('order')

    def get_lawyers(self, language):
        return Lawyer.objects.filter(language=language).order_by('order')


class BaseContentSitemap(Sitemap, ItemsGetterMixin):

    language = None
    content_type = None
    limit = 2000

    def items(self):
        return self.get_items(self.language, for_model=self.content_type)

    def lastmod(self, obj):
        return obj.created_at


class HebrewNewsSitemap(BaseContentSitemap):

    language = 'he'
    content_type = 'news'


class EnglishNewsSitemap(BaseContentSitemap):

    language = 'en'
    content_type = 'news'


class HebrewArticlesSitemap(BaseContentSitemap):

    language = 'he'
    content_type = 'articles'


class EnglishArticlesSitemap(BaseContentSitemap):

    language = 'en'
    content_type = 'articles'


class HebrewComputerLawSitemap(BaseContentSitemap):

    language = 'he'
    content_type = 'computer-law'


class LegislationComputerLawSitemap(BaseContentSitemap):

    language = 'he'
    content_type = 'legislation'


class BaseLinksSitemap(Sitemap):

    language = None

    def items(self):
        return Category.objects.filter(
            lang=self.language).order_by('tree_id', 'level')


class HebrewLinksSitemap(BaseLinksSitemap):
    language = 'he'


class EnglishLinksSitemap(BaseLinksSitemap):

    language = 'en'
