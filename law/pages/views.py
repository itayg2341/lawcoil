from django.views.generic import DetailView
from django.utils.translation import get_language

from .models import Page


class PageView(DetailView):

    def get_template_names(self):
        """Return page's template name if defined, or fallback to default
        behavior
        """
        page = self.object

        if page.template:
            return [page.template]

        return super().get_template_names()

    def get_queryset(self):
        return Page.objects.filter(language=get_language(), published=True)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['narrow_search'] = True
        return context
