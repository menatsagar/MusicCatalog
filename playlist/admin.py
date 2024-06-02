from django.contrib import admin

from playlist.models import Album, Artist, Playlist, Track, PlaylistTrack

# Register your models here.

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Playlist)
admin.site.register(PlaylistTrack)