from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from django.template.defaultfilters import striptags

from law.content.admin import SendEmailNotificationMixin
from law.content.const import CONTENT_TYPE
from law.content.models import CommonContent


class Command(SendEmailNotificationMixin, BaseCommand):

    help = 'Send watch words test message to a specified user'

    def add_arguments(self, parser):
        parser.add_argument('address', nargs='+',
                            help='Send test emails to those addresses')

    def handle(self, *args, **options):

        news_item = self.get_common_content_news_item()
        news_item_words = striptags(news_item.content).split()
        words = news_item_words[2:4]
        site = Site.objects.get_current()

        msg = self.render_words_message(site, news_item, None, words)
        self.send_message(msg, site, options['address'])

    def get_common_content_news_item(self):
        "Get the latest published news item"

        return CommonContent.objects.get_published_ordered().filter(
            ctype=CONTENT_TYPE.news.value).first()
