from allauth.account.forms import LoginForm, SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML
from django import forms
from django.urls import reverse
from django.utils.translation import gettext as _, get_language

from .models import User, ShareContact
from law.content.models import ContentCategory
from law.mailinglists.models import MailingList


class CrispyLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'login-form'
        self.helper.form_action = reverse('account_login')
        self.helper.attrs = {'novalidate': 'true'}
        self.helper.html5_required = True
        self.helper.disable_csrf = True

        self.helper.layout = Layout(
            Div(
                HTML(
                    '<p><i class="fa fa-exclamation-circle"></i>&nbsp;' +
                    '<span></span></p>'
                ),
                css_class='alert callout',
                style='display: none',
                id='login-error'
            ),
            Div(
                'login',
                'password',
                css_class="label-hidden"
            ),
            'remember',
            Div(
                Div(
                    Submit('submit_login', _('Sign In'),
                           css_class="expanded button"),
                    css_class="small-6 columns"
                ),
                Div(
                    HTML(
                        '<a class="secondary expanded button" href="' +
                        reverse('account_reset_password') + '">' +
                        _('Forgot Password?') + '</a>'
                    ),
                    css_class="small-6 columns"
                ),
                css_class='row'
            )
        )


class CrispySignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'footer-signup-form'
        self.helper.form_action = reverse('account_signup')
        self.helper.attrs = {'novalidate': 'true'}
        self.helper.html5_required = True
        self.helper.disable_csrf = True

        self.helper.layout = Layout(
            Div(
                Div('username', css_class="large-2 medium-4 columns"),
                Div('email', css_class="large-4 medium-5 columns"),
                Div('password1', css_class="large-2 medium-4 columns"),
                Div('password2', css_class="large-2 medium-5 columns"),
                Div(
                    Submit('submit_signup', _('Register'),
                           css_class="expanded dark-blue button"),
                    css_class="large-2 medium-3 columns"
                ),
                css_class='row label-hidden'
            )
        )


class UserSettingsForm(forms.ModelForm):

    categories = forms.ModelMultipleChoiceField(
        queryset=ContentCategory.objects.all(),
        required=False, widget=forms.CheckboxSelectMultiple)

    mailing_lists = forms.ModelMultipleChoiceField(
        queryset=MailingList.objects.all(),
        required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'organization', 'role',
                  'phone', 'address', 'categories', 'avatar', 'mailing_lists',
                  'watch_words']
        widgets = {
            'avatar': forms.FileInput,
            'watch_words': forms.Textarea(attrs={'rows': 5})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].queryset = ContentCategory.objects.filter(
            language=get_language()).order_by('name')
        self.initial['categories'] = self.instance.categories.all()
        self.initial['mailing_lists'] = self.instance.mailing_lists.all()

        self.fields['avatar'].widget.attrs = {'class': ''}
        self.label_suffix = ''

    def save(self, commit=True):
        super().save(commit)

        if commit and self.instance.pk:
            self.instance.categories = self.cleaned_data['categories']
            self.instance.mailing_lists = self.cleaned_data['mailing_lists']

    def clean_watch_words(self):
        words = self.cleaned_data.get('watch_words', '').splitlines()
        cleaned_words = [x.strip() for x in words if len(x.strip()) >= 4]
        return '\n'.join(cleaned_words)


ShareContactFormSet = forms.inlineformset_factory(
    User, ShareContact, fields=('name', 'email'), extra=1)
