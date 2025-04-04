import matplotlib.pyplot as plt
import io
import urllib, base64
from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Movie
from .forms import MovieForm
def index(request):
    movies = Movie.objects.all()
    
    search_query = request.GET.get('search', '')
    genre_filter = request.GET.get('genre', '')
    year_filter = request.GET.get('year', '')
    country_filter = request.GET.get('country', '')

    if search_query:
        movies = movies.filter(
            title__icontains=search_query
        ) | movies.filter(
            director__icontains=search_query
        ) | movies.filter(
            cast__icontains=search_query
        )

    if genre_filter:
        movies = movies.filter(listed_in__icontains=genre_filter)

    if year_filter:
        movies = movies.filter(release_year=year_filter)

    if country_filter:
        movies = movies.filter(country__icontains=country_filter)

    all_countries = Movie.objects.values_list('country', flat=True).distinct()
    unique_countries = set()

    for country_entry in all_countries:
        if country_entry:  
            country_list = [c.strip() for c in country_entry.split(',')]
            unique_countries.update(country_list)
    
    unique_countries = sorted(unique_countries)
    unique_countries.remove("")
    all_genres = Movie.objects.values_list('listed_in', flat=True).distinct()
    unique_genres = set()

    for genre_entry in all_genres:
        if genre_entry:  
            genre_list = [c.strip() for c in genre_entry.split(',')]
            unique_genres.update(genre_list)

    unique_genres = sorted(unique_genres)

    years = sorted(Movie.objects.values_list('release_year', flat=True).distinct())

    return render(request, 'index.html', {
        'movies': movies,
        'genres': unique_genres,
        'years': years,
        'countries': unique_countries,
        'search_query': search_query,
        'genre_filter': genre_filter,
        'year_filter': year_filter,
        'country_filter': country_filter
    })



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
    plt.close(fig)

    # -----------------------------------------------------------------

    #10 countries with highest number of titles
    top_countries = Movie.objects.filter(type='Movie') \
        .values('country') \
        .annotate(count=Count('id')) \
        .order_by('-count')[:10]

    # Prepare data for plotting
    countries = [entry['country'] for entry in top_countries]
    counts = [entry['count'] for entry in top_countries]



    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(countries, counts)
    ax.set_title("Top 10 Countries with the Most Titles")
    ax.set_xlabel("Country")
    ax.set_ylabel("Number of Titles")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save the plot to a BytesIO object to pass it to the template
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64_1 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close(fig)


    #10 top directors
    top_directors = Movie.objects.filter(type='Movie').exclude(director = "Missing Value") \
        .values('director') \
        .annotate(count=Count('id')) \
        .order_by('-count')[:10]
    
    directors = [entry['director'] for entry in top_directors]
    counts = [entry['count'] for entry in top_directors]



    plt.figure(figsize=(10,5))
    plt.bar(directors, counts)
    plt.title("Top 10 Directors")
    plt.xlabel("Director")
    plt.ylabel("Number of Releases")
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.3)

    # Save the plot to a BytesIO object to pass it to the template
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64_2 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()


    # of Netflix titles by release year
    releaseYears = Movie.objects.values_list('release_year',flat=True)
    # releaseYearsList = list(releaseYears)
    plt.figure(figsize=(10,5))
    plt.hist(releaseYears, bins=80)
    plt.title("Distrubution of Netflix Titles by Release Year")
    plt.xlabel("Release Year")
    plt.ylabel("Number of Titles")
    plt.grid(axis="y", linestyle='--')

    # Save the plot to a BytesIO object to pass it to the template
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64_3 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

    plt.close('all')
    # Pass the charts to the template
    return render(request, 'results.html', {'chart': [image_base64,image_base64_1,image_base64_2,image_base64_3]})

# def form(request):
#     movies = Movie.objects.all()
#     form = MovieForm()

#     if request.method == "POST":
#         form = MovieForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
        
#         return render(request, 'index.html', {'movies': movies, 'form':form})
