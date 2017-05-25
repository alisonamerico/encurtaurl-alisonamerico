from django.core.management.base import BaseCommand, CommandError

from shortener.models import encurtaURL

class Command(BaseCommand):
    help = 'Refreshes all encurtaURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        print(options)
        return encurtaURL.objects.refresh_shortcodes(items=options['items'])
