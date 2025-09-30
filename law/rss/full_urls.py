from django.urls import re_path

from . import feeds


urlpatterns = [
    re_path(r'^news/$', feeds.NewsFullFeed(), name='news'),
    re_path(r'^articles/$', feeds.ArticlesFullFeed(), name='articles'),
    re_path(r'^computer-law/$', feeds.ComputerLawFullFeed(), name='computer_law'),
    re_path(r'^legislation/$', feeds.LegislationFullFeed(), name='legislation'),
    re_path(r'^topics/(?P<slug>[\w-]+)/$', feeds.CategoryFullFeed(), name='categories'),
    re_path(r'^news/(?P<slug>[\w-]+)/$', feeds.NewsFullFeed(), name='news_category'),
    re_path(r'^articles/(?P<slug>[\w-]+)/$', feeds.ArticlesFullFeed(), name='articles_category'),
    re_path(r'^computer-law/(?P<slug>[\w-]+)/$', feeds.ComputerLawFullFeed(), name='computer_law_category'),
    re_path(r'^legislation/(?P<slug>[\w-]+)/$', feeds.LegislationFullFeed(), name='legislation_category'),
    re_path(r'^terms/$', feeds.TermsFeed()),
    re_path(r'^privacy/$', feeds.PrivacyFeed()),
    re_path(r'^about-site/$', feeds.AboutFeed()),
    re_path(r'^about-group/$', feeds.AboutGroupFeed()),
    re_path(r'^practice/$', feeds.PracticesFeed()),
    re_path(r'^lawyers/$', feeds.LawyersFeed()),
]
