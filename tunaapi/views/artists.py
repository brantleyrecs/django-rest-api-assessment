from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from tunaapi.models import Artist, Song

class ArtistView(ViewSet):
  
  def retrieve(self, request, pk):
    
    try:
      artist = Artist.objects.get(pk=pk)
      serializer = ArtistSerializer(artist)
      return Response(serializer.data)
    except Artist.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
  def list(self, request):
    
    artist = Artist.objects.all()
    
    song = request.query_params.get('song', None)
    if song is not None:
      artist = artist.filter(song_id=song)
    
    serializer = ArtistSerializer(artist, many=True)
    return Response(serializer.data)
  
class ArtistSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = Artist
    fields = ('id', 'name', 'age', 'bio', 'song_count', 'song')
    depth = 1
