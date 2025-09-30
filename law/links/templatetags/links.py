from django import template
from django.conf import settings

from ..models import Category


register = template.Library()


@register.simple_tag(takes_context=True)
def get_cached_links_categories(context):
    language = context.get('LANGUAGE_CODE', settings.LANGUAGE_CODE)
    return Category.get_cached_categories(language)
