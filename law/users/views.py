# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from functools import lru_cache

from braces.views import (LoginRequiredMixin, CsrfExemptMixin,
                          AjaxResponseMixin, JSONResponseMixin)
from django.urls import reverse
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.utils.translation import get_language, gettext as _
from django.views.generic import (DetailView, ListView, RedirectView,
                                  UpdateView, TemplateView, View)

from law.content.mixins import ItemsGetterMixin
from law.content.models import CommonContent
from law.core.decorators import require_post
from law.mailinglists.models import MailingList
from .forms import UserSettingsForm, ShareContactFormSet
from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class MyTopicsIndexView(LoginRequiredMixin, ListView):

    template_name = 'users/my_topics_index.html'

    def get_queryset(self):
        language = get_language()
        user = self.request.user

        return user.categories.filter(language=language)\
                              .annotate(followers_count=Count('followers'))\
                              .order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_my_topics'] = True
        return context


class MyTopicsListingView(LoginRequiredMixin, ItemsGetterMixin, TemplateView):

    template_name = 'users/my_topics.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        for_model = self.kwargs.get('content_type')
        language = get_language()
        user = self.request.user
        page = self.request.GET.get('page')
        category_slug = kwargs.get('cat_slug')
        category = get_object_or_404(user.categories, slug=category_slug,
                                     language=language)

        items = self.get_paginated_items(language, user=user, page=page,
                                         category_slug=category_slug,
                                         for_model=for_model,
                                         even_pages=True)
        cols = [items[::4], items[1::4], items[2::4], items[3::4]]
        context.update({
            'items_cols': cols,
            'items_paginator': items,
            'is_my_topics': True,
            'model_type': for_model,
            'category': category,
        })

        return context


@require_post
class ToggleSaveView(CsrfExemptMixin, ItemsGetterMixin, AjaxResponseMixin,
                     JSONResponseMixin, View):

    """Toggle save/unsave of content item"""

    def post_ajax(self, request, *args, **kwargs):

        if not request.user.is_authenticated():
            return self.render_json_response({'login_required': True}, 401)

        content_type = self.kwargs.get('content_type')
        slug = kwargs.get('slug')
        item = get_object_or_404(
            CommonContent.objects.get_for_type(content_type),
            language=get_language(), slug=slug)

        response = {
            'is_saved': None,
            'message': 'Unknown',
            'tooltip': 'Unknown',
        }

        user = self.request.user
        saved_item = user.get_saved_item(item)

        if saved_item:
            user.items.remove(item)
            response['is_saved'] = False
            response['message'] = _('Item removed from &quot;My Content&quot;')
            response['tooltip'] = _('Save to &quot;My Content&quot;')
        else:
            user.items.add(item)
            response['is_saved'] = True
            response['message'] = _('Item saved to &quot;My Content&quot;')
            response['tooltip'] = _('Remove from &quot;My Content&quot;')

        return self.render_json_response(response)


class MyContentView(LoginRequiredMixin, ItemsGetterMixin, TemplateView):

    template_name = 'users/my_content.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for_model = self.kwargs.get('content_type')
        language = get_language()
        user = self.request.user
        page = self.request.GET.get('page')
        category_slug = 'my-content'

        items = self.get_paginated_items(language, user=user, page=page,
                                         category_slug=category_slug,
                                         for_model=for_model,
                                         even_pages=True)

        cols = [items[::4], items[1::4], items[2::4], items[3::4]]

        context.update({
            'items_cols': cols,
            'items_paginator': items,
            'is_my_content': True,
            'model_type': for_model
        })

        return context


class MySettingsView(LoginRequiredMixin, UpdateView):
    template_name = 'users/my_settings.html'
    form_class = UserSettingsForm
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        url = reverse("my:settings") + '?saved=true'
        return url

    def get_object(self):
        # Only get the User record for the user making the request
        return self.request.user

    @lru_cache(maxsize=2)
    def get_formset(self):
        if self.request.method == 'POST':
            formset= ShareContactFormSet(self.request.POST, self.request.FILES,
                                         instance=self.object)
        else:
            formset = ShareContactFormSet(instance=self.object)

        if self.object.share_contacts.count():
            formset.extra = 0

        return formset

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        self.object = self.get_object()
        form = self.get_form()
        share_contacts = self.get_formset()

        if form.is_valid() and share_contacts.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_formset().save()

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('saved'):
            context['saved'] = True
        context['is_my_settings'] = True
        context['share_contacts'] = self.get_formset()

        form = context['form']
        current_selected = list(
            self.object.mailing_lists.values_list('pk', flat=True))

        if form.is_bound:
            form_selected = form.cleaned_data.get( 'mailing_lists')

            if form_selected is None:
                context['selected_mailing_lists'] = form_selected
            else:
                context['selected_mailing_lists'] = [
                    x.pk for x in form_selected]
        else:
            context['selected_mailing_lists'] = current_selected

        context['all_mailing_lists'] = list(MailingList.objects.all())

        return context
