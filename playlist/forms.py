from django import forms

from playlist.models import Playlist, PlaylistTrack

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ["title","tracks"]


class PlaylisttrackForm(forms.ModelForm):
    class Meta:
        model = PlaylistTrack
        fields = ["playlist","track"]