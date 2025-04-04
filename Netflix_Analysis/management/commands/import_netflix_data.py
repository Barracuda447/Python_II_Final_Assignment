import csv
from django.core.management.base import BaseCommand
from Netflix_Analysis.models import Movie
from datetime import datetime
import os

class Command(BaseCommand):
    help = 'Imports Netflix data from a CSV file into the database'

    def handle(self, *args, **kwargs):
        # Relative path to the CSV file
        file_path = os.path.join(os.path.dirname(__file__), '../../data/cleaned_data.csv')
        
        file_path = os.path.abspath(file_path)  # Get absolute path for ease

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'File not found at {file_path}'))
            return

        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Read the CSV file
            
            # Loop through each row in the CSV file
            for row in reader:
                
                
                # Create and save the Movie object to the database
                Movie.objects.create(
                    show_id=row['show_id'],
                    type=row['type'],
                    title=row['title'],
                    director=row['director'],
                    cast=row['cast'],
                    country=row['country'],
                    date_added=row['date_added'],
                    release_year=row['release_year'],
                    rating=row['rating'],
                    duration=row['duration'],
                    listed_in=row['listed_in']
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported Netflix data'))
