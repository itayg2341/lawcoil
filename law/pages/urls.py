from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^(?P<slug>[\w-]+)/$', views.PageView.as_view(), name='page'),
]
