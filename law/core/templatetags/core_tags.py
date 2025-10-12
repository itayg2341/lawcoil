
from django import template
from django.utils.http import urlencode
from django.utils.translation import get_language

register = template.Library()

@register.filter
def add_direction(value, arg=None):
    """
    Add direction suffix to CSS filenames for RTL languages.
    For Hebrew (RTL), changes 'style.css' to 'style_rtl.css'
    """
    language = get_language() or 'he'
    
    # Only modify for RTL languages and CSS files
    if language == 'he' and value.endswith('.css'):
        # Replace .css with _rtl.css
        return value.replace('.css', '_rtl.css')
    
    return value


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
