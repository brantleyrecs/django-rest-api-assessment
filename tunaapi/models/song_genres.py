from django.db import models
from .songs import Song
from .genres import Genre

class SongGenre(models.Model):
    """Model relationship between songs and genres"""
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='genres')
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='songs')
