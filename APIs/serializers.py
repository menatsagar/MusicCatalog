from rest_framework import serializers

from playlist.models import Album, Artist, Playlist, Track


class ArtistInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["name", "genre"]


class AlbumInfoSerializer(serializers.ModelSerializer):
    artist = ArtistInfoSerializer(many = True, read_only = True)
    class Meta:
        model = Album
        fields = ["title", "artist", "genre", "language"]

class TrackInfoSerializer(serializers.ModelSerializer):
    album = AlbumInfoSerializer(read_only=True)
    class Meta:
        model = Track
        fields = ["title", "album", "language"] 

class PlaylistInfoSerializer(serializers.ModelSerializer):
    tracks = TrackInfoSerializer(many=True, read_only=True)
    class Meta:
        model = Playlist
        fields = ["title", "tracks"]


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ["title", "tracks"]