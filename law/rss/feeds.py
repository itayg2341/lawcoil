from datetime import datetime

from django.contrib.sites.models import Site
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils.text import Truncator
from django.utils.translation import get_language, gettext as _

from law.content.const import CONTENT_TYPE
from law.content.models import CommonContent, ContentCategory
from law.lawyers.models import Lawyer
from law.pages.models import Page
from law.practices.models import PracticeArea


class RssWithImageFeedGenerator(Rss201rev2Feed):

    """Feed generator which adds title, copyright and language"""

    def add_root_elements(self, handler):
        super().add_root_elements(handler)

        site = Site.objects.get_current()
        base_url = 'https://' + site.domain
        image_path = staticfiles_storage.url('images/law.co.il_rss.gif')

        handler.addQuickElement(
            "image", '',
            {
                'url': base_url + image_path,
                'title': self.feed['title'],
                'link': base_url,
            }
        )


class CopyrightMixin:

    def feed_copyright(self):
        return 'Haim Ravia 2006-%d' % datetime.now().year

    @staticmethod
    def get_current_site():
        return Site.objects.get_current()


class BaseContentFeed(CopyrightMixin, Feed):
    feed_type = RssWithImageFeedGenerator

    # Our base class definition
    content_type = None  # Override in subclasses
    truncate_words = None  # How many words to truncate

    def items(self, obj):
        qs = CommonContent.objects.get_published_ordered().filter(
            language=get_language())

        if self.content_type:
            qs = qs.filter(ctype=self.content_type)

        if obj:
            qs = qs.filter(categories__in=[obj])

        return qs.distinct()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        description = item.content

        if self.truncate_words:
            description = Truncator(description).words(self.truncate_words,
                                                       html=True,
                                                       truncate='...')
        return description

    def item_pubdate(self, item):
        return item.created_at

    def item_categories(self, item):
        if item:
            return item.categories.all()

    def get_object(self, request, *args, **kwargs):

        slug = kwargs.get('slug')

        if not slug:
            return

        return get_object_or_404(
            ContentCategory.objects.filter(language=get_language()),
            slug=slug)


class BasePartialMixin:

    """Base feed with truncated content"""

    truncate_words = 60


class NewsFullFeed(BaseContentFeed):

    content_type = CONTENT_TYPE.news.value

    def link(self, obj):
        kwargs = {'content_type': 'news'}
        if not obj:
            url_name = 'content:index'
        else:
            url_name = 'content:category'
            kwargs['cat_slug'] = obj.slug

        return reverse(url_name, kwargs=kwargs)

    def title(self, obj):
        site = self.get_current_site()

        title = _('%s - News: Internet Law') % site.name
        if obj:
            title = '%s - %s' % (title, obj)
        return title

    def description(self, obj):
        return _(
            'News feed updates from the Internet, computer and IT law portal')


class NewsPartialFeed(BasePartialMixin, NewsFullFeed):
    pass


class ArticlesFullFeed(BaseContentFeed):

    content_type = CONTENT_TYPE.articles.value

    def link(self, obj):
        kwargs = {'content_type': 'articles'}
        if not obj:
            url_name = 'content:index'
        else:
            url_name = 'content:category'
            kwargs['cat_slug'] = obj.slug

        return reverse(url_name, kwargs=kwargs)

    def title(self, obj):
        site = self.get_current_site()

        title = _('%s - Articles: Internet Law') % site.name
        if obj:
            title = '%s - %s' % (title, obj)
        return title

    def description(self):
        return _(
            'Articles about online and computer law, from the web site of '
            'Ravice and Co., Lawyers'
        )


class ArticlesPartialFeed(BasePartialMixin, ArticlesFullFeed):
    pass


class ComputerLawFullFeed(BaseContentFeed):

    content_type = CONTENT_TYPE.computer_law.value

    def link(self, obj):
        kwargs = {'content_type': 'computer-law'}
        if not obj:
            url_name = 'content:index'
        else:
            url_name = 'content:category'
            kwargs['cat_slug'] = obj.slug

        return reverse(url_name, kwargs=kwargs)

    def title(self, obj):
        site = self.get_current_site()

        title = _('%s - Computer Laws') % site.name
        if obj:
            title = '%s - %s' % (title, obj)
        return title

    def description(self):
        return _(
            'Computer Law updates from the Internet, computer and IT law '
            'portal'
        )


class ComputerLawPartialFeed(BasePartialMixin, ComputerLawFullFeed):
    pass


class LegislationFullFeed(BaseContentFeed):

    content_type = CONTENT_TYPE.legislation.value

    def link(self, obj):
        kwargs = {'content_type': 'legislation'}
        if not obj:
            url_name = 'content:index'
        else:
            url_name = 'content:category'
            kwargs['cat_slug'] = obj.slug

        return reverse(url_name, kwargs=kwargs)

    def title(self, obj):
        site = self.get_current_site()

        title = _('%s - Legislation') % site.name
        if obj:
            title = '%s - %s' % (title, obj)
        return title

    def description(self):
        return _(
            'Legislation updates from the Internet, computer and IT law '
            'portal'
        )


class LegislationPartialFeed(BasePartialMixin, LegislationFullFeed):
    pass


class CategoryFullFeed(BaseContentFeed):

    def link(self, obj):
        if not obj:
            return reverse('home')

        return obj.get_absolute_url()

    def title(self, obj):
        site = self.get_current_site()

        title = site.name

        if obj:
            title = '%s - %s' % (title, obj)
        return title

    def description(self, obj):
        return _(
            '%s updates from the Internet, Cyber and Copyright law '
            'portal' % obj.name
        )


class CategoryPartialFeed(BasePartialMixin, CategoryFullFeed):
    pass


class BasePagesFeed(CopyrightMixin, Feed):

    feed_type = RssWithImageFeedGenerator

    def get_object(self, request, *args, **kwargs):
        return Page.objects.get(language=get_language(), slug=self.slug)

    def link(self, obj):
        return obj.get_absolute_url()

    def title(self, obj):
        return self.get_current_site().name + ' - ' + obj.title

    def items(self):
        return Page.objects.filter(language=get_language(), slug=self.slug)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content


class TermsFeed(BasePagesFeed):
    slug = 'terms'


class PrivacyFeed(BasePagesFeed):
    slug = 'privacy'


class AboutFeed(BasePagesFeed):
    slug = 'about'


class AboutGroupFeed(BasePagesFeed):
    slug = 'about-group'


class PracticesFeed(CopyrightMixin, Feed):

    feed_type = RssWithImageFeedGenerator

    def link(self):
        return reverse('practices:index')

    def title(self):
        return self.get_current_site().name + ' - ' + _('Practice Areas')

    def items(self):
        return PracticeArea.objects.filter(
            language=get_language()).order_by('order')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content


class LawyersFeed(CopyrightMixin, Feed):

    feed_type = RssWithImageFeedGenerator
    description_template = 'feeds/lawyer_description.html'

    def link(self):
        return reverse('lawyers:index')

    def title(self, obj):
        return self.get_current_site().name + ' - ' + _('Group Lawyers')

    def items(self):
        return Lawyer.objects.filter(
            language=get_language()).order_by('order')

    def item_title(self, item):
        return item.name
