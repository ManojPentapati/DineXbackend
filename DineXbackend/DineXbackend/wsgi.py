"""
WSGI config for DineXbackend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DineXbackend.DineXbackend.settings')

# Attempt to run migrations on startup (Render workaround)
try:
    django.setup()
    from django.core.management import execute_from_command_line
    import sys
    
    # Run migrations silently on startup
    try:
        execute_from_command_line(['manage.py', 'migrate', '--no-input'])
        print("Migrations completed successfully on startup")
    except Exception as e:
        print(f"Migration startup warning: {e}")
        # Don't fail the application if migrations fail
        pass
        
except Exception as e:
    print(f"Django setup warning: {e}")
    pass

application = get_wsgi_application()