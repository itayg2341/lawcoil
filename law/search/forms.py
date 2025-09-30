from datetime import timedelta

from django import forms
from django.utils.translation import gettext_lazy as _, get_language

from law.content.models import ContentCategory

SEARCH_IN_CHOICES = (
    ('all', _('All Sections')),
    ('articles', _('Articles')),
    ('news', _('News Items')),
    ('computer_law', _('Computer Laws')),
    ('legislation', _('Legislation')),
)

TIME_CHOICES = (
    ('all', _('All Content')),
    ('last_day', _('Last Day')),
    ('last_week', _('Last Week')),
    ('last_month', _('Last Month')),
    ('last_year', _('Last Year')),
)

TIME_VALUES = {
    'last_day': timedelta(days=1),
    'last_week': timedelta(weeks=1),
    'last_month': timedelta(days=31),
    'last_year': timedelta(days=365),
}


class SearchForm(forms.Form):

    search_in = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=SEARCH_IN_CHOICES,
                                  initial='all')
    articles_topic = forms.ChoiceField(required=False)
    news_topic = forms.ChoiceField(required=False)
    computer_law_topic = forms.ChoiceField(required=False)
    legislation_topic = forms.ChoiceField(required=False)
    time_frame = forms.ChoiceField(label=_('By Time:'), choices=TIME_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        category_choices = self.get_category_choices()

        self.fields['articles_topic'].choices = category_choices
        self.fields['news_topic'].choices = category_choices
        self.fields['computer_law_topic'].choices = category_choices
        self.fields['legislation_topic'].choices = category_choices

    @staticmethod
    def get_category_choices():

        language = get_language()
        all_category_choices = list(
            ContentCategory.objects.filter(language=language)
            .order_by('name')
            .values_list('slug', 'name'))

        all_category_choices.insert(0, ('all', _('All Topics')))

        return all_category_choices
