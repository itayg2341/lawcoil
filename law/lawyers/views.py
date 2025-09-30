from django.utils.translation import get_language
from django.views.generic import DetailView, RedirectView

from .models import Lawyer


class RedirectToFirstLawyerView(RedirectView):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        first = Lawyer.objects.filter(
            language=get_language()).order_by('order').first()
        return first.get_absolute_url()


class LawyerDetailView(DetailView):

    def get_queryset(self):
        return Lawyer.objects.filter(language=get_language()).order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['narrow_search'] = True
        context['lawyers'] = self.get_queryset()

        return context
