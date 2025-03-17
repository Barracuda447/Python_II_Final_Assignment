import subprocess
import os

manage_py_path = os.path.join(os.path.dirname(__file__), '..', 'manage.py')

# Run the start.bat file
subprocess.run(['python', manage_py_path, 'runserver'], shell=True)

#Just click play to run app