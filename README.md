# DineX Backend for Render Deployment

This is the Django backend for the DineX application, configured for deployment on Render.

## Deployment Instructions

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following environment variables in Render:
   - SECRET_KEY (generate a secure key)
   - DEBUG (set to False for production)
   - DATABASE_URL (if using PostgreSQL, otherwise it will use SQLite)
   - DJANGO_SUPERUSER_USERNAME (optional, default: admin)
   - DJANGO_SUPERUSER_EMAIL (optional, default: admin@example.com)
   - DJANGO_SUPERUSER_PASSWORD (optional, default: adminpassword)

4. Set the build command to:
   ```
   chmod +x build.sh && ./build.sh
   ```

5. Set the start command to:
   ```
   gunicorn DineXbackend.DineXbackend.wsgi:application
   ```

6. Add the following environment variables in your Render dashboard:
   - SECRET_KEY: [your secret key]
   - DEBUG: False
   - DATABASE_URL: [your database URL if using PostgreSQL]

## Troubleshooting Database Issues

If you encounter the "no such table: auth_user" error, it means the database migrations haven't run properly. You can manually run migrations using the Render console:

1. Go to your Render dashboard
2. Click on your service
3. Go to the "Console" tab
4. Run these commands:
   ```bash
   python manual_migrate.py
   python create_superuser.py
   ```

## Local Development

To run locally:
```bash
# Activate virtual environment
source env/Scripts/activate  # On Windows
# or
source env/bin/activate      # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python DineXbackend/manage.py migrate

# Create a superuser (optional)
python DineXbackend/manage.py createsuperuser

# Collect static files
python DineXbackend/manage.py collectstatic --noinput

# Run the server
python DineXbackend/manage.py runserver
```

## Requirements

- Python 3.11.6
- Django 5.2.7
- Other dependencies listed in requirements.txt