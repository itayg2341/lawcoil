from django import forms
from django.utils.translation import gettext_lazy as _
from .models import FeedbackMessage


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = FeedbackMessage
        fields = ('name', 'email', 'phone', 'role', 'organization', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'autofocus': 'true'}),
            'content': forms.Textarea(
                attrs={'placeholder': _('What would you like to write to us?')})
        }
