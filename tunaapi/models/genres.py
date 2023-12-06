from django.db import models
from .songs import Song

class Genre(models.Model):
  description = models.CharField(max_length=150)
  song = models.ForeignKey(Song, on_delete=models.CASCADE)
