from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.FeedbackFormView.as_view(), name='index'),
    re_path(r'^success/$', views.FeedbackSuccessView.as_view(), name='success'),
]
