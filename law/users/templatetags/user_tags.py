from ..forms import CrispyLoginForm, CrispySignupForm
from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def get_login_form(context):
    form = CrispyLoginForm()
    request = context.get('request')
    if request:
        path = getattr(request, 'path', None)
        if path:
            form.helper.form_action += '?next=' + path
    return form


@register.simple_tag
def get_signup_form():
    form = CrispySignupForm()
    form.fields['username'].widget.attrs.pop('autofocus', None)
    return form
