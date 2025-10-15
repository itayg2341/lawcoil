from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.urls import reverse
from django.template.loader import render_to_string
from django.views.generic import CreateView, TemplateView

from .models import FeedbackMessage
from .forms import FeedbackForm


class FeedbackFormView(CreateView):
    model = FeedbackMessage
    form_class = FeedbackForm
    template_name = 'contact/feedback_form.html'

    def get_initial(self):
        req = self.request
        user = req.user
        if req.method == 'GET' and user.is_authenticated:
            return {
                'name': user.name,
                'email': user.email,
                'phone': user.phone,
                'role': user.role,
                'organization': user.organization,
            }

        return super().get_initial()

    def get_success_url(self):
        return reverse('contact:success')

    def send_message(self, form):
        """Sends the message using send_email. Note that From is
        set to settings.SERVER_EMAIL and subject is prefixed with
        settings.EMAIL_SUBJECT_PREFIX (defaults to [Django])
        """

        recipients = [r[1] for r in settings.CONTACTS_RECIPIENTS]
        if recipients:
            subject = '[%s] %s' % (Site.objects.get_current().name, 'Feedback')
            context = {'object': self.object}
            email = "%(name)s <%(email)s>" % form.cleaned_data
            html_message = render_to_string('contact/email_message.html',
                                            context=context,
                                            request=self.request)
            text_message = render_to_string('contact/email_message.txt',
                                            context=context,
                                            request=self.request)
            send_mail(subject, text_message, email, recipients,
                      html_message=html_message)

    def form_valid(self, form):
        response = super().form_valid(form)
        self.send_message(form)
        return response


class FeedbackSuccessView(TemplateView):

    template_name = 'contact/feedback_success.html'
