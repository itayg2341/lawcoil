from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.RedirectToFirstPracticeView.as_view(), name='index'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.PracticeDetailView.as_view(), name='practice'),
]
