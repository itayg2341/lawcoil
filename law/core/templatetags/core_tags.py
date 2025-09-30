
from django import template
from django.utils.http import urlencode

register = template.Library()

@register.filter
def add_direction(value, arg=None):
    """Dummy add_direction filter for legacy template compatibility. Returns value unchanged."""
    return value


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
