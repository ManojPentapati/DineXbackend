from django.core.management.base import BaseCommand
from django.core.management import execute_from_command_line
from django.db import connection
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Ensure all migrations are applied and create default superuser if needed'

    def handle(self, *args, **options):
        try:
            # Check if auth_user table exists
            table_names = connection.introspection.table_names()
            
            if 'auth_user' not in table_names:
                self.stdout.write('auth_user table not found. Running migrations...')
                execute_from_command_line(['manage.py', 'migrate', '--no-input'])
                self.stdout.write(
                    self.style.SUCCESS('Successfully ran migrations')
                )
            else:
                self.stdout.write('auth_user table already exists')
                
            # Create superuser if needed
            User = get_user_model()
            username = 'admin'
            
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    email='admin@example.com',
                    password='adminpassword'
                )
                self.stdout.write(
                    self.style.SUCCESS(f'Superuser {username} created successfully')
                )
            else:
                self.stdout.write(f'Superuser {username} already exists')
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error ensuring migrations: {e}')
            )