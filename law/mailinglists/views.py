from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import signing
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from .models import MailingList


class UnsubscribeView(View):
    "Implement unsubscribe functionality"

    template_name = 'mailinglists/unsubscribe.html'

    def get_payload(self, payload):
        "Load and return the payload"

        if not payload:
            raise Http404('Missing payload')

        try:
            details = signing.loads(payload, salt=settings.PASSWORD_ENC_KEY)
        except signing.BadSignature:
            raise Http404('Invalid payload')

        return details

    def get_context(self, payload, removed=False):
        "Return the template context"

        ml_id = payload['mlid']
        mailing_list = (get_object_or_404(MailingList, pk=ml_id) if ml_id > 0
                        else None)
        return {
            'mailing_list': mailing_list,
            'email': payload['email'],
            'removed': removed,
        }

    def get(self, request, **kwargs):
        "Get the landing page for unsubscribe"

        payload = self.get_payload(kwargs.get('hash'))
        context = self.get_context(payload)

        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        "Do the actual removal"

        payload = self.get_payload(kwargs.get('hash'))
        context = self.get_context(payload, removed=True)

        users = get_user_model().objects.filter(email=context['email'])
        mailing_list = context['mailing_list']

        if mailing_list and users.exists():
            mailing_list.subscribers.remove(*users)
        elif users.exists():
            for user in users:
                user.mailing_lists.clear()

        return render(request, self.template_name, context)
