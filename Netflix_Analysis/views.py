from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Render index.html

def results(request):
    return render(request, 'results.html')  # Render results.html
