from django.views.generic import DetailView

from .models import Contributor


class ContributorView(DetailView):

    model = Contributor
