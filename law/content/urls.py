from django.urls import re_path
from . import views
from .const import (CATEGORY_URL, ITEM_URL, ITEM_WITH_CATEGORY_URL,
                    ITEM_WITH_TWO_CATEGORY_URL)


urlpatterns = [
    re_path(r'^$', views.ContentListingView.as_view(), name='index'),
    re_path(CATEGORY_URL, views.ContentListingView.as_view(), name='category'),
    re_path(ITEM_URL, views.ContentDetailView.as_view(), name='detail'),
    re_path(ITEM_WITH_CATEGORY_URL, views.RedirectWithoutCategoryView.as_view()),
    re_path(ITEM_WITH_TWO_CATEGORY_URL, views.RedirectWithoutCategoryView.as_view()),
]
