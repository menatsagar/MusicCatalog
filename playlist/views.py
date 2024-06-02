from django.shortcuts import redirect, render
from django.views import View
from django.db import transaction
from playlist.forms import PlaylistForm
from playlist.models import Playlist, PlaylistTrack, Track

# Create your views here.
class PlayListListingView(View):
    def get(self, request):
        playlists = Playlist.objects.all()
        context = {'playlists':playlists}
        return render(request, "playlist/list.html", context=context)
    
class PlaylistCreateView(View):
    form = PlaylistForm
    def get(self, request):
        
        return render(request, "playlist/create.html", {"form":self.form()})
    
    def post(self, request):
        
        data = request.POST
        form  = self.form(data)
        with transaction.atomic():
            try:
                if form.is_valid():
                    
                    playlist = Playlist.objects.create(title = data.get("title"))
                    tracks = Track.objects.filter(id__in=data.getlist("tracks"))
                    last_playlisttrack = PlaylistTrack.objects.filter(playlist=playlist).last()
                    if last_playlisttrack:
                        position = last_playlisttrack.position
                    else:
                        position = 1 
                    
                    for i in range(len(data.getlist("tracks"))):
                        playlisttrack = PlaylistTrack(playlist=playlist, track=tracks[i], position = position)
                        playlisttrack.save()    
                        position += 1
                    
                    return redirect("playlist:all-playlist")
                return render(request, "playlist/create.html", {"form":self.form(data)})
            except Exception as e:
                pass
        
class PlaylistUpdateView(View):
    form = PlaylistForm
    def get(self, request, playlist):
        playlist = Playlist.objects.get(id = playlist)
        return render (request, "playlist/update.html", {"form":self.form(instance=playlist)})
    
    def post(self, request, playlist):
        playlist = Playlist.objects.get(id = playlist)
        data = request.POST
        form = self.form(instance=playlist, data = data)
        if form.is_valid():
            form.save()
        else:
            return render (request, "playlist/update.html", {"form":self.form(instance=playlist)})

        return redirect("playlist:all-playlist")
    
class PlaylistDeleteView(View):

    def post(self, request, pk) :
        
        try:
           playlist = Playlist.objects.get(id = pk)
           playlist.delete()
           return redirect("playlist:all-playlist") 
        except Exception as e:
           pass
        return redirect(request.path)