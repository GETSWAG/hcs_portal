from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Loads all test data into the database'

    def handle(self, *args, **options):
        fixtures = [
            'users/fixtures/users.json',
            'services/fixtures/service_categories.json',
            'services/fixtures/services.json',
            'tickets/fixtures/tickets.json',
            'tickets/fixtures/ticket_comments.json',
            'announcements/fixtures/announcements.json',
        ]

        for fixture in fixtures:
            self.stdout.write(f'Loading {fixture}...')
            try:
                call_command('loaddata', fixture)
                self.stdout.write(self.style.SUCCESS(f'Successfully loaded {fixture}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error loading {fixture}: {str(e)}')) 