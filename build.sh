#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your requirements file location
pip install -r requirements.txt

# Convert static asset files
python DineXbackend/manage.py collectstatic --no-input

# Apply any outstanding database migrations
python DineXbackend/manage.py migrate