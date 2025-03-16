@echo off

:: 1. Create Virtual Environment
echo Creating virtual environment...
if not exist "..\venv" (
    python -m venv ..\venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)

:: 2. Activate Virtual Environment
echo Activating virtual environment...
call ..\venv\Scripts\activate

:: 3. Install Dependencies
echo Installing dependencies from requirements.txt...
pip install -r ..\start_process\requirements.txt

:: 4. Run Django Migrations
echo Making migrations...
python ..\manage.py makemigrations

echo Applying migrations...
python ..\manage.py migrate

:: 5. Import Netflix Data
echo Importing Netflix data...
python ..\manage.py import_netflix_data

:: 6. Run the Development Server
echo Starting development server...
python ..\manage.py runserver
