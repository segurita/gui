from optparse import make_option

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--folder',
                            action='store',
                            dest='input_folder',
                            help='Enter name of folder containing JSON files to import.'
                            )

    def handle(self, *args, **options):
        if not options['input_folder']:
            raise CommandError("Folder does not exist.")

