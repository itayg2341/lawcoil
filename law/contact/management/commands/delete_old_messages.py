from datetime import datetime, timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from law.contact.models import FeedbackMessage


class Command(BaseCommand):

    help = 'Delete old feedback messages'

    def add_arguments(self, parser):
        parser.add_argument('--days', type=int, default=7,
                            help='Number of days to keep messages for')
        parser.add_argument('--dry', action='store_true',
                            help='Dry run - does not actually delete messages')

    def handle(self, *args, **options):
        if settings.USE_TZ:
            now = timezone.now()
        else:
            now = datetime.now()

        cutoff = now - timedelta(days=options['days'])
        is_dry_run = options['dry']

        qs = FeedbackMessage.objects.filter(received_at__lte=cutoff)
        total = qs.count()

        if is_dry_run:
            self.stdout.write(f'{total} matching messages found, not deleting')
        else:
            self.stdout.write(f'Deleting {total} matching messages')
            qs.delete()
