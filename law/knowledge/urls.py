from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.KnowledgeIndex.as_view(), name='index'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.KnowledgeDetail.as_view(), name='detail'),
    re_path(r'^(?P<knowledge_slug>[\w-]+)/(?P<slug>[\w-]+)/$', views.KnowledgeItemView.as_view(), name='item'),
]
