# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views import defaults as default_views

from law.content.const import CONTENT_TYPES_RE
from law.content.views import HomeView
from law.seo.urls import urlpatterns as seo_patterns
from law.mailinglists.views import UnsubscribeView


urlpatterns = seo_patterns + [
    re_path(r'^$', HomeView.as_view(), name='home'),
    # Django Admin, use {% url 'admin:index' %}
    re_path(settings.ADMIN_URL, admin.site.urls),

    # User management
    re_path(r'^users/', include(('law.users.urls', 'users'), namespace='users')),
    re_path(r'^accounts/logout/$', LogoutView.as_view(next_page='/'),
        name="account_logout_without_confirm"),
    re_path(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    re_path(r'^links/', include(('law.links.urls', 'links'), namespace='links')),
    re_path(r'^%s/' % CONTENT_TYPES_RE,
        include(('law.content.urls', 'content'), namespace='content')),
    re_path(r'^content/',
        include(('law.content.ajax_urls', 'content_ajax'), namespace='content_ajax')),
    re_path(r'^topics/', include(('law.content.category_urls', 'topics'), namespace='topics')),
    re_path(r'^my/', include(('law.users.my_urls', 'my'), namespace='my')),
    re_path(r'^search/', include(('law.search.urls', 'search'), namespace='search')),
    re_path(r'^contact-us/', include(('law.contact.urls', 'contact'), namespace='contact')),
    re_path(r'^rss/', include(('law.rss.urls', 'rss'), namespace='rss')),
    re_path(r'^rss_full/', include(('law.rss.full_urls', 'rss_full'), namespace='rss_full')),
    re_path(r'^lawyers/', include(('law.lawyers.urls', 'lawyers'), namespace='lawyers')),
    re_path(r'^practice-areas/', include(('law.practices.urls', 'practices'), namespace='practices')),
    re_path(r'^knowledge-centers/', include(('law.knowledge.urls', 'knowledge'), namespace='knowledge')),
    re_path(r'^contributors/', include(('law.contributors.urls', 'contributors'), namespace='contributors')),
    re_path(r'^annotations/', include(('law.annotations.urls', 'annotations'), namespace='annotations')),
    re_path(r'unsubscribe/(?P<hash>[^/].*)/', UnsubscribeView.as_view(), name='unsubscribe'),
    re_path(r'^', include(('law.pages.urls', 'pages'), namespace='pages')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(
    'node_modules', document_root=str(settings.ROOT_DIR.path('node_modules')))

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        re_path(r'^400/$', default_views.bad_request),
        re_path(r'^403/$', default_views.permission_denied),
        re_path(r'^404/$', default_views.page_not_found),
        re_path(r'^500/$', default_views.server_error),
    ]

    # Add Django Debug Toolbar URLs
    import debug_toolbar
    urlpatterns = [re_path(r'^__debug__/', include(debug_toolbar.urls))] + urlpatterns
