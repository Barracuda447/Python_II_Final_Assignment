from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # home page / index
    path('results/', views.results, name='results'),  # processed results page
]
