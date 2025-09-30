from django.conf import settings
from django.db.models.expressions import RawSQL

from law.importer.management.base_import_command import BaseImportCommand
from law.importer.models import (LegacySubscribers, LegacySubscriberslists,
                                 LegacyLists)
from law.users.models import User
from law.mailinglists.models import MailingList


class Command(BaseImportCommand):
    help = 'Import mailing lists subscribers as users'

    def handle(self, *args, **options):

        self.stdout.write('Importing mailing lists subscribers as users')
        self.import_admins()

    def import_admins(self):
        decode_pass = RawSQL('decode(pass, %s)', (settings.PASSWORD_ENC_KEY,))
        decode_email = RawSQL('decode(email, %s)', (settings.PASSWORD_ENC_KEY,))
        qs = LegacySubscribers.objects.annotate(
            decoded_pass=decode_pass, decoded_email=decode_email).order_by('pk')

        for c in qs:
            decoded_email = c.decoded_email.decode('utf-8')
            self.stdout.write('* %s <%s>' % (str(c), decoded_email))

            u, created = User.objects.get_or_create(email=decoded_email)

            if created:
                u.name = c.name
                u.username = decoded_email[:30]
                splitted_name = c.name.split(None, 1)
                if len(splitted_name) > 1:
                    u.first_name, u.last_name = splitted_name
                else:
                    u.first_name = u.last_name = c.name
                u.set_password(c.decoded_pass.decode())

            u.watch_words = c.words
            u.save()

            old_lists_pks = LegacySubscriberslists.objects.filter(
                subscriber_id=c.pk).values_list('list_id', flat=True)
            old_lists_names = list(LegacyLists.objects.filter(
                pk__in=old_lists_pks).values_list('name', flat=True))
            user_lists = MailingList.objects.filter(name__in=old_lists_names)

            u.mailing_lists = user_lists

            self.stdout.write('    Found %d lists' % u.mailing_lists.count())
