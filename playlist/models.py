import uuid
from django.db import models

# Create your models here.

class Activity(models.Model):

  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    mark_as_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True



class Artist(Activity):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    dob = models.DateField(blank=True, null=True)

    def __str__(self): 
        return self.name


class Album(Activity):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    artist = models.ManyToManyField(Artist, related_name='artists')
    genre = models.CharField(max_length= 30)
    language = models.CharField(max_length=30)

    def __str__(self): 
        return self.title


class Track(Activity):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name='album_tracks', on_delete=models.CASCADE)
    language = models.CharField(max_length=30)

    def __str__(self): 
        return self.title

class Playlist(Activity):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    tracks = models.ManyToManyField(Track, related_name='track_in_playlists', through="PlaylistTrack")


    def __str__(self): 
        return self.title
    
class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    track =    models.ForeignKey(Track, on_delete=models.CASCADE)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']