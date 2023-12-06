from django.db import models
from .artists import Artist

class Song(models.Model):
  title = models.CharField(max_length=50)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  album = models.CharField(max_length=50)
  length = models.IntegerField()
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
