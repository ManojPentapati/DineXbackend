@echo off
echo Starting Django server...

REM Activate virtual environment
call env\Scripts\activate.bat

REM Start the Django development server
python DineXbackend\manage.py runserver

pause