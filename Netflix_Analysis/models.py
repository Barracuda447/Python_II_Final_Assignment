from django.db import models

class Movie(models.Model):
    show_id = models.CharField(max_length=100)
    # type can be 'Movie' or 'TV Show'
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255, null=True, blank=True)
    cast = models.TextField(null=True, blank=True)  # A TextField to store actors since there could be many
    country = models.CharField(max_length=255, null=True, blank=True)
    date_added = models.CharField(max_length=30, null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    rating = models.CharField(max_length=10, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)  # Duration of movie or number of tv show seasons

    def __str__(self):
        return self.title
