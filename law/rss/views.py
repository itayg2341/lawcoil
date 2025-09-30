from django.views.generic import TemplateView


class RSSListingView(TemplateView):

    template_name = 'feeds/feeds_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['narrow_search'] = True
        context['is_site_updates'] = True

        return context
