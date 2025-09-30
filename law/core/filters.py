from django.contrib.admin.filters import RelatedFieldListFilter
from django.utils.encoding import smart_str
from django.utils.html import conditional_escape, mark_safe
from mptt.settings import DEFAULT_LEVEL_INDICATOR


class TreeDropdownFilter(RelatedFieldListFilter):
    template = 'admin_filters/tree_dropdown_filter.html'

    def _get_level_indicator(self, obj):
        level = getattr(obj, obj._mptt_meta.level_attr)
        return mark_safe(conditional_escape(DEFAULT_LEVEL_INDICATOR) * level)

    def label_from_instance(self, obj):
        """
        Creates labels which represent the tree level of each node when
        generating option labels.
        """
        level_indicator = self._get_level_indicator(obj)
        return mark_safe(level_indicator + ' ' +
                         conditional_escape(smart_str(obj)))

    def field_choices(self, field, request, model_admin):
        model = field.related_model().__class__

        choices = [
            (n.pk, self.label_from_instance(n)) for n in model.objects.all()]

        return choices


class RelatedDropdownFilter(RelatedFieldListFilter):
    template = 'admin_filters/tree_dropdown_filter.html'
