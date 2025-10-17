import os
import django
from django.contrib.auth import get_user_model
from django.db import transaction

try:
    # Set up Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DineXbackend.DineXbackend.settings')
    django.setup()

    User = get_user_model()

    # Create a superuser if it doesn't exist
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'adminpassword')

    # Check if user already exists
    if not User.objects.filter(username=username).exists():
        with transaction.atomic():
            User.objects.create_superuser(username, email, password)
            print(f'Superuser {username} created successfully!')
    else:
        print(f'Superuser {username} already exists.')
        
except Exception as e:
    print(f'Error creating superuser: {e}')
    print('This might be because migrations have not run yet or database is not ready')