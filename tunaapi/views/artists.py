from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.db.models import Count
from tunaapi.models import Artist, Song

class ArtistView(ViewSet):
  
  def retrieve(self, request, pk):
    
    try:
      artist = Artist.objects.annotate(
        song_count=Count('songs')
    ).get(pk=pk)
      serializer = ArtistSerializer(artist)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Artist.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
  def list(self, request):
    
    artists = Artist.objects.annotate(song_count=Count('songs')).all()
    
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
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
        return Response('Artist edited', status=status.HTTP_200_OK)

class ArtistSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = Artist
    fields = ('id', 'name', 'age', 'bio', 'song_count', 'song')
    depth = 1
