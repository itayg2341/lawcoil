from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.RedirectToFirstLawyerView.as_view(), name='index'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.LawyerDetailView.as_view(), name='lawyer'),
]
