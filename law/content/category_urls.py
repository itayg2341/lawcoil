from django.urls import re_path

from . import views
from .const import CATEGORY_URL

FOLLOW_URL = CATEGORY_URL[:-1] + 'follow/$'
UNFOLLOW_URL = CATEGORY_URL[:-1] + 'unfollow/$'


urlpatterns = [
    re_path(CATEGORY_URL, views.CategoryView.as_view(), name='category'),
    re_path(FOLLOW_URL, views.CategoryFollowView.as_view(), name='follow'),
    re_path(UNFOLLOW_URL, views.CategoryUnfollowView.as_view(), name='unfollow'),
]
