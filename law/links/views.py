from django.views.generic import RedirectView, TemplateView
from django.utils.translation import get_language, gettext as _
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import Category


class LinksCategoriesMixin:
    "Gets the root categories into the context"

    def get_root_categories(self):
        """docstring for get_root_links"""
        lang = get_language()
        return Category.get_cached_categories(lang)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['narrow_search'] = True
        context['is_links'] = True
        context['root_categories'] = self.get_root_categories()

        return context


class LinksIndexView(LinksCategoriesMixin, RedirectView):

    'Redirects to first available category'

    permanent = False
    query_string = False

    def get_redirect_url(self):
        """docstring for get_redirect_url"""
        first_category = self.get_root_categories().first()
        return first_category.get_absolute_url()


class LinksCategoryView(LinksCategoriesMixin, TemplateView):

    template_name = 'links/links.html'

    def get_category(self):
        """Get the category based on `slugs_path` kwarg"""

        slugs_path = self.kwargs.get('slugs_path')

        if not slugs_path:
            raise Http404(_('Category not found'))

        slugs = [s.strip() for s in slugs_path.split('/') if s.strip()]
        total_slugs = len(slugs)

        category = None
        current_category = None
        language = get_language()

        for idx, slug in enumerate(slugs, 1):
            if idx == 1:
                current_category = get_object_or_404(Category, slug=slug,
                                                     level=idx, lang=language)
            else:
                current_category = get_object_or_404(
                    current_category.get_children(), slug=slug)
            if idx == total_slugs and current_category:
                category = current_category

        if category:
            return category
        else:
            raise Http404(_('Category not found'))

    def get_context_data(self, **kwargs):
        """docstring for get_context_"""

        context = super().get_context_data(**kwargs)
        category = self.get_category()
        context['category'] = category
        context['category_ancestors'] = category.ancestors[:-1]
        context['root_category'] = category.ancestors[0]
        context['child_categories'] = category.get_children()
        context['links'] = category.links.order_by(
            'hebname' if get_language == 'he' else 'engname')

        return context
