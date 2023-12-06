from django.db import models
from .songs import Song

class Artist(models.Model):
  name = models.CharField(max_length=50)
  age = models.IntegerField()
  bio = models.CharField(max_length=150)
  song_count = models.IntegerField()
  songs = models.ForeignKey(Song, on_delete=models.CASCADE)
