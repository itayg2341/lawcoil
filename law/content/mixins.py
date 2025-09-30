from django.conf import settings
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.shortcuts import get_list_or_404, get_object_or_404

from law.content.models import ContentCategory
from law.core.paginator import UnequalFirstPagePaginator
from .const import CONTENT_TYPE
from .models import CommonContent


class ItemsGetterMixin:

    @staticmethod
    def get_items(language, user=None, category_slug=None, for_model=None):

        qs = None
        categories = None

        if category_slug == 'my-content':
            qs = user.items.filter(language=language)
        elif category_slug == 'my-topics':
            if user and user.is_authenticated:
                categories = user.categories.filter(language=language)
            if not categories or not categories.exists():
                categories = ContentCategory.objects.get_regular_categories(
                    language)
        elif category_slug == 'hot-topics':
            if language == 'he':
                categories = get_list_or_404(ContentCategory, language=language)
            else:
                categories = ContentCategory.objects.get_hot_categories(language)
        elif category_slug:
            categories = get_list_or_404(ContentCategory, language=language,
                                         slug=category_slug)
        else:
            categories = get_list_or_404(ContentCategory, language=language)

        if qs is None:
            qs = CommonContent.objects.filter(
                categories__in=categories, published=True).distinct()

        if for_model:
            ctype = CommonContent.objects.get_content_type_value(for_model)
            qs = qs.filter(ctype=ctype)

        if category_slug == 'my-topics':
            qs = qs.exclude(ctype=CONTENT_TYPE.computer_law.value)

        qs = qs.select_related().prefetch_related().order_by('-created_at')

        return qs

    def get_paginated_items(self, language, user, category_slug, page,
                            for_model=None, even_pages=False):

        items_qs = self.get_items(language, user, category_slug, for_model)
        if category_slug == 'my-topics':
            first_page_size = settings.ITEMS_PER_PAGE
            rest_page_size = settings.ITEMS_PER_PAGE
        elif category_slug == 'hot-topics':
            first_page_size = settings.ITEMS_PER_PAGE
            rest_page_size = settings.ITEMS_FOR_REST_OF_HOT_TOPICS
        elif even_pages:
            first_page_size = rest_page_size = settings.ITEMS_FOR_REST_OF_PAGES
        else:
            first_page_size = settings.ITEMS_FOR_FIRST_PAGE
            rest_page_size = settings.ITEMS_FOR_REST_OF_PAGES

        paginator = UnequalFirstPagePaginator(items_qs, rest_page_size,
                                              first_page_size=first_page_size)

        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = []

        return items

    @staticmethod
    def get_category(slug):
        return get_object_or_404(ContentCategory, slug=slug)
