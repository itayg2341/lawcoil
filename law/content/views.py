import datetime
from urllib.parse import quote_plus

from braces.views import (JSONResponseMixin, AjaxResponseMixin,
                          LoginRequiredMixin, CsrfExemptMixin)
from django.conf import settings
from django.contrib.sites.models import Site
from django.core import signing
from django.urls import reverse
from django.http import Http404
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.utils import timezone
from django.utils.translation import get_language, gettext as _
from django.views.generic import View, TemplateView, DetailView, RedirectView

from law.content.const import CONTENT_TYPE
from law.core.decorators import require_post
from .mixins import ItemsGetterMixin
from .models import CommonContent, CONTENT_TYPE_DICT


class HomeView(ItemsGetterMixin, TemplateView):

    "Home page"

    template_name = 'content/index.html'

    @staticmethod
    def get_feeds():
        site = Site.objects.get_current()
        return [
            {
                'url': reverse('rss:news'),
                'title': _('%s - News: Internet Law') % site.domain,
            },
            {
                'url': reverse('rss:articles'),
                'title': _('%s - Articles: Internet Law') % site.domain,
            },
            {
                'url': reverse('rss:computer_law'),
                'title': _('%s - Computer Laws') % site.domain,
            },
            {
                'url': reverse('rss:legislation'),
                'title': _('%s - Legislation') % site.domain,
            },
        ]

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        language = get_language()
        user = self.request.user

        page = self.request.GET.get('page')

        regular_items = self.get_paginated_items(
            language, user=user, page=page, category_slug='my-topics')

        for_model = 'computer-law' if language == 'he' else None
        hot_items = self.get_paginated_items(language, user=user, page=page,
                                             category_slug='hot-topics',
                                             for_model=for_model)
        cols = [[], [], []]

        for index, item in enumerate(regular_items):
            if index == 4:
                cols[2].append(item)
            elif index == 5:
                cols[0].append(item)
            else:
                cols[index % 3].append(item)

        context['regular_items_cols'] = cols
        context['hot_items'] = hot_items
        context['regular_items_paginator'] = regular_items
        context['hot_items_paginator'] = hot_items
        context['feeds'] = self.get_feeds()
        context['is_index'] = True
        return context


class CategoryView(ItemsGetterMixin, TemplateView):

    "Category page"

    template_name = 'content/category.html'

    @staticmethod
    def get_feeds(category):
        site = Site.objects.get_current()

        kwargs = {'slug': category.slug}
        return [
            {
                'url': reverse('rss:categories', kwargs=kwargs),
                'title': '%s - %s' % (site.domain, category.name),
            },
        ]

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        language = get_language()
        user = self.request.user
        page = self.request.GET.get('page')
        category_slug = self.kwargs.get('cat_slug')
        category = self.get_category(category_slug)

        items = self.get_paginated_items(language, user=user, page=page,
                                         category_slug=category_slug)

        if items:
            cols = [[], [], [], []]
            for index, item in enumerate(items):
                if index == 2:
                    cols[3].append(item)
                else:
                    cols[index % 4].append(item)
        else:
            cols = None

        context.update({
            'items_cols': cols,
            'items_paginator': items,
            'category': category,
            'feeds': self.get_feeds(category)
        })

        return context


class ItemsGetterAJAXView(ItemsGetterMixin, JSONResponseMixin, View):

    def get(self, request, *args, **kwargs):

        category_slug = request.GET.get('category')
        for_model = request.GET.get('type')
        language = get_language()
        page = request.GET.get('page')

        if category_slug == 'hot-topics' and language == 'he':
            for_model = 'computer-law'

        if not category_slug and not for_model:
            return HttpResponseBadRequest('missing category or item type')

        items = self.get_paginated_items(language, user=request.user,
                                         page=page,
                                         category_slug=category_slug,
                                         for_model=for_model)

        if category_slug == 'hot-topics':
            template_name = 'content/_hot_item.html'
        else:
            template_name = 'content/_listing_item.html'

        template = get_template(template_name)

        rendered_items = []

        next_page = (items.next_page_number()
                     if items.has_next() else None)

        for item in items:
            html = template.render({
                'item': item,
                'category': item.category,
                'words': 60,
                'heading_level': 3,
            }, request)
            rendered_items.append(html)

        response = {
            'rendered_items': rendered_items,
            'next_page': next_page,
            'category': category_slug,
            'type': for_model,
        }
        return self.render_json_response(response)


class ContentListingView(ItemsGetterMixin, TemplateView):

    template_name = 'content/listing.html'

    def get_feeds(self, category):
        site = Site.objects.get_current()

        url_name = None
        title = None

        if self.kwargs['content_type'] == 'news':
            url_name = 'rss:news'
            title = _('%s - News: Internet Law') % site.domain

        elif self.kwargs['content_type'] == 'articles':
            url_name = 'rss:articles'
            title = _('%s - Articles: Internet Law') % site.domain

        elif self.kwargs['content_type'] == 'computer-law':
            url_name = 'rss:computer_law'
            title = _('%s - Computer Laws') % site.domain

        elif self.kwargs['content_type'] == 'legislation':
            url_name = 'rss:legislation'
            title = _('%s - Legislation') % site.domain

        if url_name:
            result = [{'url': reverse(url_name), 'title': title}]

            if category:
                cat_url = reverse(url_name + '_category',
                                  kwargs={'slug': category.slug})
                cat_title = title + ' - ' + category.name
                result.append({'url': cat_url, 'title': cat_title})

            return result

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        language = get_language()
        category_slug = self.kwargs.get('cat_slug')
        if category_slug:
            category = self.get_category(category_slug)
        else:
            category = None

        page = self.request.GET.get('page')

        items = self.get_paginated_items(
            language, user=self.request.user, page=page,
            category_slug=category_slug, for_model=self.kwargs['content_type'])

        if items:
            cols = [[], [], [], []]
            for index, item in enumerate(items):
                if index == 2:
                    cols[3].append(item)
                else:
                    cols[index % 4].append(item)
        else:
            cols = None

        content_type = self.kwargs['content_type']
        verbose_name = CommonContent.objects.get_verbose_name_for_content_type(
            content_type)
        context.update({
            'items_cols': cols,
            'items_paginator': items,
            'model_verbose_name': verbose_name,
            'model_name': content_type,
            'item_type': content_type,
            'category': category,
            'feeds': self.get_feeds(category),
        })

        return context


class ContentDetailView(DetailView):

    template_name = 'content/detail.html'
    item_type = None

    CTYPE_TO_ADMIN = {
        'news': 'newsitem',
        'articles': 'article',
        'computer_law': 'computerlaw',
        'legislation': 'legislation',
    }

    def get_object(self, queryset=None):

        try:
            item_date = datetime.date(
                int(self.kwargs['year']),
                int(self.kwargs['month']),
                int(self.kwargs['day']),
            )
        except (ValueError, TypeError):
            raise Http404(_('Invalid date'))

        start = datetime.datetime.combine(item_date, datetime.time.min)
        end = datetime.datetime.combine(
            item_date, datetime.time.max) + datetime.timedelta(days=1)

        if settings.USE_TZ:
            start = timezone.make_aware(start, timezone.get_current_timezone())
            end = timezone.make_aware(end, timezone.get_current_timezone())

        return get_object_or_404(
            CommonContent.objects.get_for_type(self.kwargs['content_type']),
            slug=self.kwargs['slug'], created_at__range=(start, end))

    def get_is_saved(self):
        """The user saved this item ?

        :return: boolean"""

        user = self.request.user

        if user.is_anonymous:
            return False

        return user.get_saved_item(self.object) is not None

    def get_admin_url(self):
        """
        Returns the admin url for the edited item or `None` If the user does
        not have edit permissions.
        """

        user = self.request.user

        ctype = CONTENT_TYPE_DICT.get(self.object.ctype)
        admin_model = self.CTYPE_TO_ADMIN.get(ctype)

        if not ctype or not admin_model:
            return None

        perm = 'change_' + admin_model
        if not user.is_staff or not user.has_perm(perm):
            return None

        from django.urls import reverse
        return reverse('admin:content_%s_change' % admin_model,
                       args=(self.object.pk, ))

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        categories = self.object.categories.all()

        full_path = quote_plus(self.request.build_absolute_uri())
        twitter_url = 'https://twitter.com/home?status=' + quote_plus(
            self.object.title + ' ') + full_path
        facebook_url = 'https://www.facebook.com/sharer/sharer.php?u=' \
            + full_path
        linkedin_url = 'https://www.linkedin.com/sharing/share-offsite/?url=' + full_path
        gplus_url = 'https://plus.google.com/share?url=' + full_path

        annotator_url = None

        if self.request.user.is_authenticated:
            annotator_uri = signing.dumps(
                [self.object.pk, self.request.user.pk],
                key=settings.PASSWORD_ENC_KEY)
            context.update({'annotator_uri': annotator_uri})

        context.update({
            'categories': categories,
            'contributors': self.object.contributors.all(),
            'model_verbose_name':  self.object.get_verbose_name(),
            'model_url_name': self.object.url_content_type,
            'narrow_search': True,
            'show_blurb': self.object.ctype == CONTENT_TYPE.articles.value,
            'item_type': self.kwargs['content_type'],
            'twitter_url': twitter_url,
            'facebook_url': facebook_url,
            'linkedin_url': linkedin_url,
            'full_path': full_path,
            'gplus_url': gplus_url,
            'is_saved': self.get_is_saved(),
            'admin_url': self.get_admin_url(),
            'similar_items': list(self.object.get_similar(2)),
            'create_slug_uri': self.object.get_annotation_uri(),
        })

        return context


class RedirectWithoutCategoryView(RedirectView):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        """Redirect without category slug, for compatibility with old site."""

        parts = self.request.path.split('/')

        category_slug_index = 2

        if kwargs.get('parent_cat_slug'):
            del parts[category_slug_index]

        if kwargs.get('cat_slug'):
            del parts[category_slug_index]

        return '/'.join(parts)


@require_post
class CategoryFollowView(CsrfExemptMixin, ItemsGetterMixin,
                         AjaxResponseMixin, JSONResponseMixin,
                         LoginRequiredMixin, View):

    def post_ajax(self, request, *args, **kwargs):

        category = self.get_category(kwargs.get('cat_slug'))
        user = request.user

        if not category.followers.filter(id=user.id).exists():
            category.followers.add(user)
            response = {
                'success': True,
                'content': '<span class="follow">%s</span>' % _('Following')
            }
        else:
            response = {'success': False, 'content': _('Already Following')}

        return self.render_json_response(response)


@require_post
class CategoryUnfollowView(CsrfExemptMixin, ItemsGetterMixin,
                           AjaxResponseMixin, JSONResponseMixin,
                           LoginRequiredMixin, View):

    def post_ajax(self, request, *args, **kwargs):

        category = self.get_category(kwargs.get('cat_slug'))
        user = request.user

        if category.followers.filter(id=user.id).exists():
            category.followers.remove(user)
            response = {
                'success': True,
                'content': '<span>%s</span>' % _('Not Following')
            }
        else:
            response = {'success': False, 'content': _('Not Following')}

        return self.render_json_response(response)
