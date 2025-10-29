@echo off
echo Starting Adolat AI Backend Server...
echo ==================================
echo Make sure you have activated your virtual environment
echo and installed all dependencies before running this script.
echo.
echo To install dependencies, run:
echo pip install -r requirements.txt
echo.
echo To run migrations, run:
echo python manage.py migrate
echo.
echo Starting server on http://127.0.0.1:8000
echo Press CTRL+C to stop the server
echo ==================================
echo.
python manage.py runserver