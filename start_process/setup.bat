@echo off



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
