@echo off
echo Setting up Django backend...

REM Activate virtual environment
call env\Scripts\activate.bat

REM Install required packages
pip install -r requirements.txt

REM Run migrations
python DineXbackend\manage.py makemigrations
python DineXbackend\manage.py migrate

echo Setup complete! Run 'python DineXbackend\manage.py runserver' to start the server.
pause