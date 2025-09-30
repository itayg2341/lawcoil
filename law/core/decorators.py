from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST as post_only


def require_post(view):
    view.dispatch = method_decorator(post_only)(view.dispatch)
    return view
