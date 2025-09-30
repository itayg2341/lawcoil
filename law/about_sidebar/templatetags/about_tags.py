from django import template

from law.pages.models import Page
from law.lawyers.models import Lawyer
from law.practices.models import PracticeArea


register = template.Library()


@register.inclusion_tag('about_sidebar/about_sidebar.html', takes_context=True)
def render_about_sidebar(context, expanded=None):

    language = context.get('LANGUAGE_CODE', 'he')

    about_page = Page.objects.get(slug='about', language=language)
    about_group_page = Page.objects.get(slug='about-group', language=language)
    lawyers = Lawyer.objects.filter(language=language).order_by('order')
    practices = PracticeArea.objects.filter(language=language).order_by(
        'order')

    return {
        'about_page': about_page,
        'about_group_page': about_group_page,
        'lawyers': lawyers,
        'practices': practices,
        'expanded': expanded,
    }
