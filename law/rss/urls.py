from django.urls import re_path

from . import feeds, views


urlpatterns = [
    re_path(r'^$', views.RSSListingView.as_view(), name='index'),
    re_path(r'^news/$', feeds.NewsPartialFeed(), name='news'),
    re_path(r'^articles/$', feeds.ArticlesPartialFeed(), name='articles'),
    re_path(r'^computer-law/$', feeds.ComputerLawPartialFeed(), name='computer_law'),
    re_path(r'^legislation/$', feeds.LegislationPartialFeed(), name='legislation'),
    re_path(r'^topics/(?P<slug>[\w-]+)/$', feeds.CategoryPartialFeed(), name='categories'),
    re_path(r'^news/(?P<slug>[\w-]+)/$', feeds.NewsPartialFeed(), name='news_category'),
    re_path(r'^articles/(?P<slug>[\w-]+)/$', feeds.ArticlesPartialFeed(), name='articles_category'),
    re_path(r'^computer-law/(?P<slug>[\w-]+)/$', feeds.ComputerLawPartialFeed(), name='computer_law_category'),
    re_path(r'^legislation/(?P<slug>[\w-]+)/$', feeds.LegislationPartialFeed(), name='legislation_category'),
]
