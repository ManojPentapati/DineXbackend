#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your requirements file location
pip install -r requirements.txt

# Show Python and Django version
echo "Python version:"
python --version
echo "Django version:"
python -m django --version

# Show current directory and files
echo "Current directory:"
pwd
echo "Files in current directory:"
ls -la

# Show migration status before migration
echo "Current migration status:"
python DineXbackend/manage.py showmigrations || echo "showmigrations failed"

# Convert static asset files
echo "Collecting static files..."
python DineXbackend/manage.py collectstatic --no-input -c

# Apply migrations using our custom command
echo "Ensuring migrations are applied..."
python DineXbackend/manage.py ensure_migrations

# Show migration status after migration
echo "Migration status after migration:"
python DineXbackend/manage.py showmigrations || echo "showmigrations failed"