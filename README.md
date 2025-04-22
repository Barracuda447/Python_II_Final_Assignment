How to set up app to work:

1. Open new terminal

2. cd start_process

3. ./setup.bat


To start the app you have 2 choices:

1. From start_process directory enter "./start.bat" in terminal and hit enter

2. Click on the VS Code play button in this file: start_process\Start_Button.py







Our Requirements:

1. Project Overview
In this project, you will demonstrate your understanding of key Python programming concepts 
by performing data analysis on a real-world dataset and developing a web application to 
showcase your findings. You will work with the Netflix Movies and TV Shows dataset, utilizing 
Python libraries such as Numpy, Pandas, Matplotlib, and Django. 
2. Project Objectives
• Apply Python programming concepts, including object-oriented programming, modules, 
and virtual environments.
• Utilize Numpy, Pandas, and Matplotlib for data analysis and visualization.
• Develop a Django web application to present analysis results dynamically.
• Integrate SQLite as the database for the web application.
3. Project Requirements
3.1 Software and Tools
• Visual Studio Code: Primary Integrated Development Environment (IDE) for 
development.
• SQLite: Database management system for storing and retrieving data.
• Django: Python-based web framework for building the web application.
• Python Packages: Numpy, Pandas, Matplotlib, Scipy, Django, SQLite3.
• Version Control: Use Git and GitHub for managing project versions and collaboration.
3.2 Dataset
Obtain the dataset from Kaggle: Netflix Movies and TV Shows Dataset
3.3 Tasks and Instructions
1. Setup and Installation
• Download the Netflix Movies and TV Shows dataset from Kaggle.
• Set up a Python virtual environment to manage project dependencies.
• Install necessary Python packages using pip install -r requirements.txt.
2. Data Analysis
• Load the dataset into a Pandas DataFrame
• Perform data cleaning and exploratory analysis using NumPy and Pandas: 
o Check for missing values
o Fill missing values in categorial columns
o Drop rows with missing date_added
o Count the number of unique values in each column
o Find the most frequent movie type
o Find the oldest and newest movies.
o Calculate the year with the most title released.
• Create visualizations using Matplotlib to answer the following: 
o Which country has the highest number of Netflix titles?
o What are the top 10 directors featured on Netflix?
o Plot a histogram showing distribution of Netflix titles by release year.
3. Create a new Django project and an application within it.
• Define models in models.py to map to the dataset’s structure.
• Create a user-friendly interface with the following features: 
o Search functionality to filter content by title, director, or cast.
o Dropdowns and checkboxes for filtering content by genre, release year, or 
country.
• Implement URL routing and templates for presenting the result.
4. Documentation and Reporting
• Code Documentation: Add meaningful comments and docstrings to explain key 
functionalities.
• Report
5. Submission
• Code Files: Include all Python scripts and Django project files.
• Requirements File: Provide a requirements.txt listing all dependencies.
• Report: Attach a well-structured PDF report.
• Packaging: Zip all required files into a single .zip folder for submission.
4. Additional Resources
• Django Documentation: Django Docs
• SQLite Documentation: SQLite Docs
• Pandas Documentation: Pandas Docs
• Matplotlib Documentation: Matplotlib Docs
• Numpy Documentation: Numpy Docs
• Visual Studio Code Documentation: VS Code Docs
• GitHub Guide: GitHub Docs
5. Assessment Criteria
• Functionality: The application should perform data analysis accurately and display 
results effectively through the web interface.
• Code Quality: Write clear, well-organized, and commented code following best 
practices.
• Use of Python Packages: Proper implementation of Numpy, Pandas, Matplotlib, and 
Django.
• User Interface: A simple, intuitive, and responsive web interface.
• Report Quality: A clear, detailed, and well-structured report explaining the entire 
development process.
• Presentation: You will present your project in the last week of the semester. The 
presentation should include: 
o A live demonstration of the web application.
o Explanation of key features and findings from data analysis
