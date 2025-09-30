from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import KnowledgeCenter, KnowledgeCenterItem


class KnowledgeMixin:
    @staticmethod
    def get_knowledge_context():
        centers = KnowledgeCenter.objects.order_by('order')
        return {'is_knowledge': True, 'centers': centers}


class KnowledgeIndex(KnowledgeMixin, ListView):
    model = KnowledgeCenter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_knowledge_context())
        return context


class KnowledgeDetail(KnowledgeMixin, DetailView):
    model = KnowledgeCenter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_knowledge_context())

        items = list(
            self.object.items.filter(display_in_listing=True).order_by('order'))

        if items:
            cols = [items[::4], items[1::4], items[2::4], items[3::4]]
        else:
            cols = None

        context['cols'] = cols
        return context


class KnowledgeItemView(KnowledgeMixin, DetailView):

    model = KnowledgeCenterItem

    def get_object(self, queryset=None):
        kwargs = self.kwargs
        return self.model.objects.select_related().get(
            knowledge_center__slug=kwargs.get('knowledge_slug'),
            slug=kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_knowledge_context())

        return context
