from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'items/$', views.ItemsGetterAJAXView.as_view(),
        name='ajax_items'),
]
