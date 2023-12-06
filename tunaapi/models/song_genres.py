from django.db import models
from ..models.songs import Song
from ..models.genres import Genre

class SongGenre(models.Model):
    """Model relationship between songs and genres"""
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='genres')
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='songs')
