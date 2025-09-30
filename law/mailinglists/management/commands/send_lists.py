from datetime import datetime

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand, CommandError
from django.core import signing
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import override
from django.utils.html import strip_tags

from law.mailinglists.models import MailingList


class Command(BaseCommand):

    help = 'Send mailing lists emails if needed'

    template_name = 'mailinglists/message.html'

    def add_arguments(self, parser):
        parser.add_argument('--addresses', nargs='*',
                            help='Send just test emails to those addresses')
        parser.add_argument('--count', type=int,
                            help='Ignore dates and send the count of items')
        parser.add_argument('--list-id', type=int,
                            help='Send just this mailing list')

    def handle(self, *args, **options):

        self.stdout.write('Checking lists')
        self.verbosity = options['verbosity']

        self.test_addresses = options.get('addresses')
        self.count_of_items_to_send = options.get('count')

        if self.count_of_items_to_send and not self.test_addresses:
            raise CommandError('`count` specified without `addresses`')

        if settings.USE_TZ:
            self.now = timezone.now()
        else:
            self.now = datetime.now()

        self.site = Site.objects.get_current()
        self.stdout.write('[%s] Sending mailing lists' % self.now)

        list_id = options.get('list_id')
        lists = (MailingList.objects.all() if not list_id
                 else MailingList.objects.filter(pk=list_id))
        for mailing_list in lists:
            self.check_mailing_list(mailing_list)

    def check_mailing_list(self, mailing_list):

        self.stdout.write('* Checking mailing list %s:' % (str(mailing_list)))

        if self.verbosity > 1:
            self.stdout.write('  - last sent %s' % mailing_list.last_sent)

        qs = mailing_list.get_content_queryset(
            self.now, count=self.count_of_items_to_send)
        if mailing_list.send_days:
            self.stdout.write('  - List is sent by days')
        elif mailing_list.send_count:
            self.stdout.write('  - List is sent by count')
        else:
            self.stdout.write('  - Unknown list send method, aborting!')
            return

        items = list(qs)

        if items:
            self.stdout.write('  - Items to send: %d' % len(items))
            self.send_emails(mailing_list, items)
        else:
            self.stdout.write('  - No items to send')

        if not self.test_addresses:
            if self.verbosity > 1:
                self.stdout.write('  - Setting last checked to %s' % self.now)

            mailing_list.last_checked = self.now

            if items:
                if self.verbosity > 1:
                    self.stdout.write('  - Setting last sent to %s' % self.now)
                mailing_list.last_sent = self.now

            mailing_list.save()
        elif self.verbosity > 1:
            self.stdout.write(
                '  - NOT Setting last checked to %s, test mode' % self.now)

    def render_mailing_list_template(self, mailing_list, items, email):

        unsubscribe_list = {'mlid': mailing_list.pk, 'email': email}
        unsubscribe_all = {'mlid': -1, 'email': email}

        list_hash = signing.dumps(unsubscribe_list,
                                  salt=settings.PASSWORD_ENC_KEY)
        all_hash = signing.dumps(unsubscribe_all,
                                 salt=settings.PASSWORD_ENC_KEY)

        context = {
            'items': items,
            'mailing_list': mailing_list,
            'site': self.site,
            'list_hash': list_hash,
            'all_hash': all_hash,
        }

        with override('he'):
            message = render_to_string(self.template_name, context=context)

        return message

    def send_emails(self, mailing_list, items):
        subscribers = self.test_addresses or list(
            mailing_list.subscribers.filter(send_newsletters=True)
            .exclude(email__isnull=True)
            .values_list('email', flat=True))

        if not subscribers:
            if self.verbosity > 1:
                self.stdout.write('  - No subscribers, aborting!')
            return

        for email in subscribers:
            try:
                message = self.render_mailing_list_template(mailing_list, items,
                                                            email)
                text_message = strip_tags(message)
                subject = '%s - %s' % (self.site.name, mailing_list.name)
                sender = 'noreply@' + self.site.domain

                msg = EmailMultiAlternatives(subject, text_message, sender, [email])
                msg.attach_alternative(message, 'text/html')
                # msg.content_subtype = 'html'

                if self.verbosity > 1:
                    self.stdout.write('  - Sending message to %s' % email)
                msg.send()
            except Exception as e:
                self.stderr.write('  - Error sending message to %s' % email)
