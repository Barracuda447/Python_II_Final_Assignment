import matplotlib.pyplot as plt
import io
import urllib, base64
from django.shortcuts import render
from .models import Movie

def index(request):
    return render(request, 'index.html')  # Render index.html

def results(request):
    
    # Get counts of movies and TV shows
    movie_count = Movie.objects.filter(type='Movie').count()
    tv_show_count = Movie.objects.filter(type='TV Show').count()

    # Create the bar chart using matplotlib
    fig, ax = plt.subplots()
    ax.bar(['Movies', 'TV Shows'], [movie_count, tv_show_count])
    ax.set_title('Movies vs TV Shows')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')

    # Save the plot to a BytesIO object to pass it to the template
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Pass the chart to the template
    return render(request, 'results.html', {'chart': image_base64})
