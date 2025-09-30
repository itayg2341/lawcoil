from django.urls import include, re_path
from django.contrib.sitemaps import views as sitemaps_views
from django.http import HttpResponse

from .views import (PagesSitemap, HebrewNewsSitemap, EnglishNewsSitemap,
                    HebrewArticlesSitemap, EnglishArticlesSitemap,
                    HebrewComputerLawSitemap, LegislationComputerLawSitemap,
                    HebrewLinksSitemap, EnglishLinksSitemap)

ROBOTS_TXT = """# All robots allowed
User-agent: *
Disallow:

# Sitemap files
Sitemap: https://www.law.co.il/sitemap.xml"""

sitemaps = {
    'pages': PagesSitemap,
    'news-he': HebrewNewsSitemap,
    'news-en': EnglishNewsSitemap,
    'articles-he': HebrewArticlesSitemap,
    'articles-en': EnglishArticlesSitemap,
    'computerlaw-he': HebrewComputerLawSitemap,
    'legislation-he': LegislationComputerLawSitemap,
    'links-he': HebrewLinksSitemap,
    'links-en': EnglishLinksSitemap,
}

urlpatterns = [
    re_path(r'^sitemap\.xml$', sitemaps_views.index, {'sitemaps': sitemaps}),
    re_path(r'^sitemap-(?P<section>.+)\.xml$', sitemaps_views.sitemap,
        {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^robots.txt',
        lambda x: HttpResponse(ROBOTS_TXT, content_type='text/plain')),
]
