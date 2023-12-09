from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import SongGenre, Song, Genre

class SongGenreView(ViewSet):
  
  def retrieve(self, request, pk):
      """GET Single Song Genre"""
      song_genre = SongGenre.objects.get(pk=pk)
      serializer = SongGenreSerializer(song_genre)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
  def list(self, request):
      """GET All Song Genres"""
      songs = SongGenre.objects.all()
      serializer = SongGenreSerializer(songs, many=True)
      response_data = serializer.data
      print("SongGenreView response_data:", response_data)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
  def create(self, request):
        """CREATE Song Genre"""
        song = Song.objects.get(pk = request.data["song"])
        genre = Genre.objects.get(pk = request.data["genre"])
        song_genre = SongGenre.objects.create(
          song=song,
          genre=genre
        )
    
        # try:
        #     song = Song.objects.get(id=song)
        # except Song.DoesNotExist:
        #     return Response(
        #         {"error": f"Song with id {song} does not exist."},
        #         status=status.HTTP_404_NOT_FOUND
        #     )
          
        # try:
        #     genre = Genre.objects.get(id=genre)
        # except Genre.DoesNotExist:
        #     return Response(
        #         {"error": f"Genre with id {genre} does not exist."},
        #         status=status.HTTP_404_NOT_FOUND
        #     )

        # song_genre = SongGenre.objects.create(
        #     song_id=song,
        #     genre_id=genre,
        #     )
        
        serializer = SongGenreSerializer(song_genre)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
  def update(self, request, pk):
        """UPDATE Song Genre"""
        song_genre = SongGenre.objects.get(pk=pk)
        song_genre.song = Song.objects.get(pk=request.data["song_id"])
        song_genre.genre = Genre.objects.get(pk=request.data["genre_id"])
        song_genre.save()
        return Response('Song Genre updated', status=status.HTTP_200_OK)
      
  def destroy(self, request, pk):
        """DELETE Song Genre"""
        song_genre = SongGenre.objects.get(pk=pk)
        song_genre.delete()
        return Response('Song Genre deleted', status=status.HTTP_204_NO_CONTENT)
      
class SongGenreSerializer(serializers.ModelSerializer):
    """JSON serializer for song genres"""
    class Meta:
        model = SongGenre
        fields = ('id', 'song', 'genre')
