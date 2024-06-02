from django.urls import path

from playlist.views import PlayListListingView, PlaylistCreateView, PlaylistUpdateView, PlaylistDeleteView
app_name = "playlist"

urlpatterns = [
    path("", PlayListListingView.as_view(), name="all-playlist"), 
    path("create/", PlaylistCreateView.as_view(), name="create-playlist"), 
    path("update/<uuid:playlist>/", PlaylistUpdateView.as_view(), name="update-playlist"), 
    path("delete/<uuid:pk>/", PlaylistDeleteView.as_view(), name="delete-playlist"), 
    ]
