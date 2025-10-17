#!/usr/bin/env python
"""
Manual migration script for Render deployment issues
"""
import os
import django
from django.core.management import execute_from_command_line

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DineXbackend.DineXbackend.settings')
django.setup()

if __name__ == '__main__':
    try:
        print("Running Django migrations...")
        execute_from_command_line(['manage.py', 'migrate', '--no-input'])
        print("Migrations completed successfully!")
    except Exception as e:
        print(f"Error running migrations: {e}")
        import traceback
        traceback.print_exc()