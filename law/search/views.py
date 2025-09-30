from functools import lru_cache
from datetime import datetime

from digg_paginator import DiggPaginator
from django.conf import settings
from django.db.models import Q
from django.utils.translation import get_language
from django.views.generic import ListView

from law.content.const import CONTENT_TYPE
from law.content.models import CommonContent, ContentCategory
from law.contributors.models import Contributor
from .forms import SearchForm, TIME_VALUES


class SearchView(ListView):

    template_name = 'search/search.html'
    paginate_by = settings.ITEMS_FOR_REST_OF_PAGES
    paginator_class = DiggPaginator
    MIN_VALID_QUERY_LENGTH = 3

    @property
    @lru_cache(2)
    def search_term(self):
        return self.request.GET.get('q', '').strip()

    @property
    def has_enough_query(self):
        return len(self.search_term) >= self.MIN_VALID_QUERY_LENGTH

    @staticmethod
    def filter_by_type(qs, form):
        data = form.cleaned_data
        search_in = data['search_in']
        if search_in not in ('articles', 'news', 'computer_law',
                             'legislation'):
            return qs

        qs = qs.filter(ctype=CONTENT_TYPE[search_in].value)

        topic_slug = data.get(search_in + '_topic', '').strip()
        if topic_slug and topic_slug != 'all':
            cats = ContentCategory.objects.filter(slug=topic_slug,
                                                  language=get_language())
            if cats:
                qs = qs.filter(categories__in=cats)
        return qs

    @staticmethod
    def filter_by_time(qs, form):
        data = form.cleaned_data
        time_frame = data['time_frame']

        if time_frame not in TIME_VALUES:
            return qs

        qs = qs.filter(created_at__gt=datetime.now() - TIME_VALUES[time_frame])
        return qs

    def get_matching_contribs(self):
        return Contributor.objects.filter(name__icontains=self.search_term)

    def get_queryset(self):
        if not self.has_enough_query:
            return CommonContent.objects.none()

        qs = CommonContent.objects.filter(language=get_language(),
                                          published=True)

        filters = (
            Q(title__icontains=self.search_term) |
            Q(content__icontains=self.search_term) |
            Q(short_desc__icontains=self.search_term)
        )

        contribs = self.get_matching_contribs()
        if contribs:
            filters |= Q(contributors__in=contribs)

        qs = qs.filter(filters)

        form = self.get_form()

        if form.is_bound:
            qs = self.filter_by_type(qs, form)
            qs = self.filter_by_time(qs, form)

        qs = qs.prefetch_related().distinct()
        return qs

    @lru_cache(2)
    def get_form(self):
        form = SearchForm(self.request.GET)

        if form.is_valid():
            return form

        return SearchForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page = context.get('page_obj')
        cols = [page[::4], page[1::4], page[2::4], page[3::4]]

        context.update({
            'has_enough_query': self.has_enough_query,
            'search_term': self.search_term,
            'items_cols': cols,
            'form': self.get_form()
        })

        return context
