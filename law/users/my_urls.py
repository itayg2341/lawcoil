from django.urls import re_path

from . import views
from law.content.const import CONTENT_TYPES_RE


urlpatterns = [
    re_path(r'^topics/$', views.MyTopicsIndexView.as_view(), name='topics'),
    re_path(r'^topics/(?P<cat_slug>[\w-]+)/$', views.MyTopicsListingView.as_view(),
        name='topics_category'),
    re_path(r'^topics/(?P<cat_slug>[\w-]+)/%s/$' % CONTENT_TYPES_RE,
        views.MyTopicsListingView.as_view(), name='topics_by_type'),
    re_path(r'^content/$', views.MyContentView.as_view(), name='content'),
    re_path(r'^content/%s/$' % CONTENT_TYPES_RE, views.MyContentView.as_view(),
        name='content_by_type'),
    re_path(r'^settings/$', views.MySettingsView.as_view(), name='settings'),
    re_path(r'save-toggle/%s/(?P<slug>[\w-]+)/$' % CONTENT_TYPES_RE,
        views.ToggleSaveView.as_view(), name="save_toggle")
]
