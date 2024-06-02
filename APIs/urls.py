from django.urls import path
from .views import PlaylistDetailsView, PlaylistDeleteAPIView, CreatePlaylistAPIView , UpdatePlaylistAPIView
app_name = "APIs"

urlpatterns = [
    path("", PlaylistDetailsView.as_view(), name="list-playlist-api"), 
    path("create/", CreatePlaylistAPIView.as_view(), name="create-playlist-api"), 
    path("update/", UpdatePlaylistAPIView.as_view(), name="update-playlist-api"), 
    path("delete/", PlaylistDeleteAPIView.as_view(), name="delete-playlist-api"), 
    ]
