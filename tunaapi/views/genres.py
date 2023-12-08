from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Genre, SongGenre

class GenreView(ViewSet):
  def retrieve(self, request, pk):
        """GET Single Genre"""
        genre = Genre.objects.prefetch_related('songs').get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
  def list(self, request):
      """GET All Genres"""
      genres = Genre.objects.all()
      serializer = GenreSerializer(genres, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
      
  def create(self, request):
        """CREATE Genre"""
        genre = Genre.objects.create(
            description=request.data["description"],
        )
        
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
  def update(self, request, pk):
        """UPDATE Genre"""
        genre = Genre.objects.get(pk=pk)
        genre.description = request.data["description"]
        genre.save()
        return Response('Genre edited', status=status.HTTP_200_OK)
      
  def destroy(self, request, pk):
        """DELETE Genre"""
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response('Genre deleted', status=status.HTTP_204_NO_CONTENT) 
      
class SongGenreSerializer(serializers.ModelSerializer):
    """
    JSON serializer for song genres
    """
    id = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    artist_id = serializers.SerializerMethodField()
    album = serializers.SerializerMethodField()
    length = serializers.SerializerMethodField()
    
    class Meta:
        model = SongGenre
        fields = ('id', 'title', 'artist_id', 'album', 'length')
        
    def get_id(self, obj):
        """Get that id"""
        return obj.song_id.id

    def get_title(self, obj):
        """Get that title"""
        return obj.song_id.title

    def get_artist_id(self, obj):
        """Get that artist"""
        return obj.song_id.artist_id.id

    def get_album(self, obj):
        """Get that album"""
        return obj.song_id.album

    def get_length(self, obj):
        """Get that length"""
        return obj.song_id.length
      
class GenreSerializer(serializers.ModelSerializer):
    """
    JSON serializer for genres
    """
    songs = SongGenreSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ('id', 'description', 'songs')
        depth = 1
