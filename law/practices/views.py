from django.utils.translation import get_language
from django.views.generic import DetailView, RedirectView

from .models import PracticeArea
from law.lawyers.models import Lawyer


class RedirectToFirstPracticeView(RedirectView):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        first = PracticeArea.objects.filter(
            language=get_language()).order_by('order').first()
        return first.get_absolute_url()


class PracticeDetailView(DetailView):

    def get_queryset(self):
        return PracticeArea.objects.filter(
            language=get_language()).order_by('order')

    @staticmethod
    def get_lawyers():
        return Lawyer.objects.filter(
            language=get_language()).order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['narrow_search'] = True
        context['practices'] = self.get_queryset()
        context['lawyers'] = self.get_lawyers()

        return context
