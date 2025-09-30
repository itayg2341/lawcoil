from django.db import models
from django.http import Http404
from django.utils.translation import gettext_lazy as _

from .const import CONTENT_TYPE


class ContentCategoryManager(models.Manager):

    def get_hot_categories(self, language):
        """Get the categories marked as `is_hot`"""
        return self.filter(language=language, is_hot=True)

    def get_regular_categories(self, language):
        """Get categories without `is_hot`"""
        return self.filter(language=language).exclude(is_hot=True)


def _get_normalized_content_type(content_type_str):
    return content_type_str.replace('-', '_')


class CommonContentManager(models.Manager):

    @staticmethod
    def get_content_type_value(content_type_str):
        normalized_content_type = _get_normalized_content_type(
            content_type_str)

        try:
            return CONTENT_TYPE[normalized_content_type].value
        except KeyError:
            raise Http404(_('Item type does not exist: %s') % content_type_str)

    def get_for_type(self, content_type_str):

        return self.get_queryset().filter(
            ctype=self.get_content_type_value(content_type_str))

    @staticmethod
    def get_verbose_name_for_content_type(content_type_str):
        normalized_content_type = _get_normalized_content_type(
            content_type_str)
        names = {
            'articles': _('Articles'),
            'news': _('News Items'),
            'computer_law': _('Computer Laws'),
            'legislation': _('Legislation'),
        }

        return names.get(normalized_content_type)

    def get_published_ordered(self):
        return self.get_queryset().filter(
            published=True).order_by('-created_at')


class ArticleManager(models.Manager):
    """Article proxy class manager"""

    def get_queryset(self):
        """Gets just the articles from CommonContent"""
        return super().get_queryset().filter(ctype=CONTENT_TYPE.articles.value)

    def create(self, **kwargs):
        kwargs['ctype'] = CONTENT_TYPE.articles.value
        return super().create(**kwargs)


class NewsItemManager(models.Manager):
    """NewsItem proxy class manager"""

    def get_queryset(self):
        """Gets just the articles from CommonContent"""
        return super().get_queryset().filter(ctype=CONTENT_TYPE.news.value)

    def create(self, **kwargs):
        kwargs['ctype'] = CONTENT_TYPE.news.value
        return super().create(**kwargs)


class ComputerLawManager(models.Manager):
    """ComputerLaw proxy class manager"""

    def get_queryset(self):
        """Gets just the articles from CommonContent"""
        return super().get_queryset().filter(
            ctype=CONTENT_TYPE.computer_law.value)

    def create(self, **kwargs):
        kwargs['ctype'] = CONTENT_TYPE.computer_law.value
        return super().create(**kwargs)


class LegislationManager(models.Manager):
    """Legislation proxy class manager"""

    def get_queryset(self):
        """Gets just the articles from CommonContent"""
        return super().get_queryset().filter(
            ctype=CONTENT_TYPE.legislation.value)

    def create(self, **kwargs):
        kwargs['ctype'] = CONTENT_TYPE.legislation.value
        return super().create(**kwargs)
