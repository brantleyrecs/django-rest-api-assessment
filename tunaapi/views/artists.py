from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.db.models import Count
from tunaapi.models import Artist, Song

class ArtistView(ViewSet):
  
  def retrieve(self, request, pk):
    
    try:
      artist = Artist.objects.get(pk=pk)
      serializer = ArtistSerializer(artist)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Artist.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
  def list(self, request):
    
    try:
      artists = Artist.objects.all()
      serializer = ArtistSerializer(artists, many=True)
      return Response(serializer.data)
    except Artist.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def create(self, request):
    """creating an artist"""
    artist = Artist.objects.create(
      name=request.data["name"],
      age=request.data["age"],
      bio=request.data["bio"],
    )
    
    serializer = ArtistSerializer(artist)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
        """UPDATE an Artist"""
        artist = Artist.objects.get(pk=pk)
        artist.name = request.data["name"]
        artist.age = request.data["age"]
        artist.bio = request.data["bio"]
        artist.save()   
        
        serializer = ArtistSerializer(artist)  
        return Response(serializer.data, status=status.HTTP_200_OK)

class ArtistSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = Artist
    fields = ('id', 'name', 'age', 'bio')
    depth = 1

  # def get_songs(self, obj):
  #       """Get them songs"""
  #       songs = obj.songs.all()  # Get all the related songs for the given artist
  #       serializer = SongSerializer(songs, many=True)  # Create a new SongSerializer instance for serializing the list of songs
  #       return serializer.data  # Return the serialized data of the list of songs
