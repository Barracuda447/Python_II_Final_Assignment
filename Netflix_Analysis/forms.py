from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['show_id','type','title','director','cast','country','date_added','release_year','rating','duration']