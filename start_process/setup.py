import subprocess
import os
import sys

# Function to run shell commands
def run_command(command):
    """Executes a shell command and returns the result"""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(f"Error: {result.stderr}")
        sys.exit(1)
    else:
        print(f"Successfully ran command: {command}")
        print(result.stdout)

# Paths (relative to `start_process`)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # This is start_process directory
PROJECT_DIR = os.path.join(BASE_DIR, '..')  # The parent directory of start_process (Final_Project)

# 1. Create the virtual environment if it doesn't exist
def create_virtualenv():
    """Creates a virtual environment if it doesn't exist"""
    venv_path = os.path.join(PROJECT_DIR, 'venv')
    if not os.path.exists(venv_path):
        print("Creating virtual environment...")
        run_command(f'python -m venv {venv_path}')
    else:
        print("Virtual environment already exists.")

# 2. Install dependencies from requirements.txt
def install_dependencies():
    """Installs dependencies from requirements.txt"""
    requirements_path = os.path.join(BASE_DIR, 'requirements.txt')  # relative path to requirements.txt
    venv_python = os.path.join(PROJECT_DIR, 'venv', 'Scripts', 'python')  # relative path to python inside venv
    print("Installing dependencies...")
    run_command(f'{venv_python} -m pip install -r {requirements_path}')

# 3. Make migrations
def make_migrations():
    """Makes migrations for the Django app"""
    print("Making migrations...")
    venv_python = os.path.join(PROJECT_DIR, 'venv', 'Scripts', 'python')  # relative path to python inside venv
    run_command(f'{venv_python} manage.py makemigrations')

# 4. Apply migrations
def apply_migrations():
    """Applies migrations to the database"""
    print("Applying migrations...")
    venv_python = os.path.join(PROJECT_DIR, 'venv', 'Scripts', 'python')  # relative path to python inside venv
    run_command(f'{venv_python} manage.py migrate')

# 5. Import Netflix data
def import_data():
    """Imports the data into the database"""
    print("Importing data...")
    venv_python = os.path.join(PROJECT_DIR, 'venv', 'Scripts', 'python')  # relative path to python inside venv
    run_command(f'{venv_python} manage.py import_netflix_data')

# 6. Run the Django development server
def run_server():
    """Starts the development server"""
    print("Starting the development server...")
    venv_python = os.path.join(PROJECT_DIR, 'venv', 'Scripts', 'python')  # relative path to python inside venv
    run_command(f'{venv_python} manage.py runserver')

# Method to run everything needed before starting the server
def create():
    """Run everything needed before starting the server"""
    install_dependencies()
    make_migrations()
    apply_migrations()
    import_data()

# Method to create virtualenv and do everything that the create method does
def venv_create():
    """Create virtualenv and do everything that the create method does"""
    create_virtualenv()
    install_dependencies()
    make_migrations()
    apply_migrations()
    import_data()

# Method to run the server after setup. seems redundant but is entirely for simplifying start process
def start():
    run_server()
