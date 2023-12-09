from django.db import models
from .songs import Song
from .genres import Genre

class SongGenre(models.Model):
    """Model relationship between songs and genres"""
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
