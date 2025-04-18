from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Initialize ParadeDB extension'
    
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("CREATE EXTENSION IF NOT EXISTS paradedb")
            self.stdout.write("ParadeDB extension installed")