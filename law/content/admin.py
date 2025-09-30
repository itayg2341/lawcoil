from django.contrib import admin
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse
from django.db.models.functions import Length
from django.template.defaultfilters import striptags
from django.template.loader import render_to_string
from django.utils.translation import override, gettext as _
from django.utils.text import slugify

from .const import CONTENT_TYPE
from .models import (ContentCategory, Article, ComputerLaw, NewsItem,
                     Legislation)
from law.core.filters import RelatedDropdownFilter


@admin.register(ContentCategory)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'language', 'slug', 'color', 'icon_css_class', 'is_hot')
    list_display = ('name', 'slug', 'icon_css_class', 'is_hot', 'language')
    list_filter = ('is_hot', 'language')
    list_editable = ('is_hot', )

    class Media:
        css = {
            'all': ('css/django_admin_rtl_fixes.css', )
        }
        js = ('js/admin_adjust.js', )


class SendEmailNotificationMixin:

    template_name = 'content/mailinglist_words.html'

    def notify_if_needed(self, obj):
        if obj.email_notified or not obj.published:
            return False

        search_fields = ('title', 'content', 'sub_title', 'short_desc')
        joined_content = ''.join(
            [striptags(getattr(obj, f) or '') for f in search_fields])

        from law.users.models import User

        users = User.objects.annotate(
            words_len=Length('watch_words')).filter(words_len__gte=3)

        site = Site.objects.get_current()
        for user in users:
            words = user.watch_words.splitlines()

            found = [w for w in words if joined_content.find(w) > -1]

            if found:
                message = self.render_words_message(site, obj, user, found)
                self.send_message(message, site, [user.email])

        obj.email_notified = True
        obj.save()

    def send_message(self, message, site, emails):
        text_message = striptags(message)

        subject = '%s - %s' % (site.name, _('Watch Words'))
        sender = 'noreply@' + site.domain

        msg = EmailMultiAlternatives(
            subject, text_message, sender, emails)
        msg.attach_alternative(message, 'text/html')
        msg.content_subtype = 'html'

        msg.send()

    def render_words_message(self, site, obj, user, words):

        context = {
            'user': user,
            'words': ', '.join(words),
            'item': obj,
            'site': site,
        }

        with override('he'):
            message = render_to_string(self.template_name, context=context)

        return message


class ContentInChangeListMixin:

    full_article_template_name = 'content/_full_article_in_admin.html'
    list_per_page = 20
    filter_horizontal = ('categories', )

    def full_article(self, obj):
        app_label, model_name = obj._meta.app_label, obj._meta.model_name
        url = reverse('admin:{}_{}_change'.format(app_label, model_name),
                      args=(obj.pk,))

        context = {
            'admin_change_url': url,
            'object': obj,
            'direction': 'rtl' if obj.language == 'he' else 'ltr',
            'lang_start': 'right' if obj.language == 'he' else 'left',
            'lang_end': 'left' if obj.language == 'he' else 'right',
        }

        return render_to_string(self.full_article_template_name,
                                context=context)
    full_article.short_description = _('Content')

    def get_list_display(self, request):
        """Make sure our full_article won't break popup content selection."""
        is_popup = request.GET.get('_popup')

        if not is_popup:
            return self.list_display

        self.list_display_links = ('title', )
        return [x if x != 'full_article' else 'title'
                for x in self.list_display]


class CommonContentAdmin(SendEmailNotificationMixin, ContentInChangeListMixin,
                         admin.ModelAdmin):
    _type_for_save = None

    date_hierarchy = 'created_at'
    list_filter = (
        'published',
        'language',
        ('categories', RelatedDropdownFilter),
        ('contributors', RelatedDropdownFilter),
    )
    search_fields = ['title', 'content']
    list_display_links = None
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        css = {
            'all': ('css/django_admin_rtl_fixes.css', )
        }
        js = ('js/admin_adjust.js', )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.ctype = self._type_for_save
        super().save_model(request, obj, form, change)
        self.notify_if_needed(obj)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        def full_clean(self_inner):
            new_data = self_inner.data.copy()
            if new_data.get('slug', '').strip():
                new_data['slug'] = slugify(new_data['slug'])

            if (self._type_for_save == CONTENT_TYPE.legislation.value
                    and not new_data.get('content')):
                new_data['content'] = '<p></p>'

            self_inner.data = new_data
            super(form, self_inner).full_clean()

        form.full_clean = full_clean
        return form


@admin.register(Article)
class ArticleAdmin(CommonContentAdmin):

    _type_for_save = CONTENT_TYPE.articles.value

    fields = ('title', 'sub_title', 'slug', 'created_at', 'short_desc',
              'content', 'language', 'published', 'contributors',
              'categories')
    list_display = ('full_article', 'created_at', 'published',
                    'facebook_check_link', 'language')


@admin.register(ComputerLaw)
class ComputerLawAdmin(CommonContentAdmin):

    _type_for_save = CONTENT_TYPE.computer_law.value

    fields = ('title', 'slug', 'created_at', 'attachment', 'url', 'content',
              'language', 'published', 'contributors', 'categories')
    list_display = ('full_article', 'created_at', 'published',
                    'facebook_check_link', 'language')


@admin.register(Legislation)
class LegislationAdmin(CommonContentAdmin):

    _type_for_save = CONTENT_TYPE.legislation.value

    fields = ('title', 'slug', 'created_at', 'attachment', 'content',
              'language', 'published', 'contributors', 'categories')
    list_display = ('full_article', 'created_at', 'published',
                    'facebook_check_link', 'language')


@admin.register(NewsItem)
class NewsAdmin(CommonContentAdmin):

    _type_for_save = CONTENT_TYPE.news.value

    fields = ('title', 'slug', 'created_at', 'content', 'language',
              'published', 'contributors', 'categories')
    list_display = ('full_article', 'created_at', 'published',
                    'facebook_check_link', 'language')
