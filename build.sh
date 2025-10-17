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

# Show migration status
echo "Current migration status:"
python DineXbackend/manage.py showmigrations

# Convert static asset files
python DineXbackend/manage.py collectstatic --no-input

# Apply any outstanding database migrations
echo "Running migrations..."
python DineXbackend/manage.py migrate --no-input

# Create superuser if it doesn't exist
echo "Creating superuser if needed..."
python create_superuser.py

# Show migration status after migration
echo "Migration status after migration:"
python DineXbackend/manage.py showmigrations