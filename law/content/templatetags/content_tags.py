from django import template
from django.template.defaultfilters import stringfilter

from law.content.models import ContentCategory

register = template.Library()


@register.simple_tag(takes_context=True)
def get_cached_generic_categories(context):
    language = context['LANGUAGE_CODE']
    return ContentCategory.get_cached_categories(language)


@register.filter
def is_followed_by(category, user):
    return category.followers.filter(id=user.id).exists()


@register.inclusion_tag('content/_listing_item.html', takes_context=True)
def listing_item(context, item, **kwargs):
    """Renders a content item in a listing page.

    Optional keyword params:

    :param words integer: Words to truncate (default: 60)
    :param compact boolean: Smaller display - no date, readmore etc.
                            (default: False)

    """
    language = context['LANGUAGE_CODE']
    compact = kwargs.get('compact', False)
    return {
        'LANGUAGE_CODE': language,
        'item': item,
        'category': item.category,
        'words': kwargs.get('words', 60),
        'compact': compact,
        'heading_level': 4 if compact else 3,
    }


@register.filter
@stringfilter
def cut_till_bracket(value):
    return value.split('(')[0]
