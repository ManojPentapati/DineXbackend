#!/usr/bin/env python
"""
Database check script for Render deployment issues
"""
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DineXbackend.DineXbackend.settings')
django.setup()

from django.db import connection
from django.contrib.auth import get_user_model

try:
    # Check if we can connect to the database
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        print("Database connection successful!")
        
    # Check if auth tables exist
    User = get_user_model()
    table_names = connection.introspection.table_names()
    
    auth_tables = [table for table in table_names if table.startswith('auth_')]
    print(f"Auth tables found: {auth_tables}")
    
    if 'auth_user' in table_names:
        print("auth_user table exists!")
        user_count = User.objects.count()
        print(f"Number of users in database: {user_count}")
    else:
        print("auth_user table does not exist!")
        
    print(f"All database tables: {table_names}")
    
except Exception as e:
    print(f"Error checking database: {e}")
    import traceback
    traceback.print_exc()