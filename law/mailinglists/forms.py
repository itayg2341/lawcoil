from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import gettext_lazy as _

from .models import Subscriber, MailingList


class SubscriberAdminForm(forms.ModelForm):

    lists = forms.ModelMultipleChoiceField(
        queryset=MailingList.objects.all(),
        required=False,
        label=_('Mailing Lists'),
        widget=FilteredSelectMultiple(verbose_name=_('Mailing Lists'),
                                      is_stacked=False)
    )

    class Meta:
        model = Subscriber
        fields = ('username', 'email', 'send_newsletters', 'first_name',
                  'last_name', 'lists', 'watch_words')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['lists'].initial = self.instance.mailing_lists.all()

    def save(self, commit=True):
        subscriber = super().save(commit=False)

        if commit:
            subscriber.save()

        if subscriber.pk:
            subscriber.mailing_lists = self.cleaned_data['lists']
            self.save_m2m()

        return subscriber
