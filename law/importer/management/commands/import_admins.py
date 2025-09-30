from django.conf import settings
from django.db.models.expressions import RawSQL

from law.importer.management.base_import_command import BaseImportCommand
from law.importer.models import LegacyAdmin
from law.users.models import User

ADMIN_EMAIL_MAPS = {
    'haim12': 'ravia@law.co.il',
    'meirke': 'mkriheli@gmail.com',
    'talk2me': 'TKaplan@PearlCohen.com',
    'DotanLaw': 'DHammer@PearlCohen.com',
    'nmatarasso': 'NMatarasso@PearlCohen.com',
}


class Command(BaseImportCommand):
    help = 'Import Admins'

    def handle(self, *args, **options):

        self.stdout.write('Importing admins')
        self.import_admins()

    def import_admins(self):
        decode_sql = RawSQL('decode(pass, %s)', (settings.PASSWORD_ENC_KEY,))
        qs = LegacyAdmin.objects.annotate(
            decoded_pass=decode_sql).order_by('pk')

        for c in qs:
            self.stdout.write('* ' + str(c))

            u, _ = User.objects.get_or_create(username=c.login)
            u.is_superuser = c.candel == 'y'
            u.is_staff = u.is_superuser or c.op == 'y'
            u.name = c.name
            splitted_name = c.name.split(None, 1)
            u.first_name, u.last_name = splitted_name
            u.set_password(c.decoded_pass.decode())

            u.email = ADMIN_EMAIL_MAPS.get(c.login)

            u.save()
