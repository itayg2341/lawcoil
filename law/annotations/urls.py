from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.RootAnnotationView.as_view(), name='root'),
    re_path(r'^api/create/$', views.APIAnnotationView.as_view(), name='create'),
    re_path(r'^api/search/$', views.SearchAnnotationView.as_view(), name='search'),
    re_path(r'^api/(?P<annotation_id>[0-9a-f-]+)/$',
        views.UpdateDeleteAnnotationView.as_view(), name='update_delete')
]
