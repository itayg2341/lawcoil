from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.LinksIndexView.as_view(), name='index'),
    re_path(r'(?P<slugs_path>.*)', views.LinksCategoryView.as_view(), name='category'),
]
