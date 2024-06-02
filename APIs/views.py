from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from django.db import transaction

from APIs.serializers import PlaylistInfoSerializer, PlaylistSerializer
from playlist.models import Playlist, PlaylistTrack, Track
from utils.custom_response import APIResponse
from utils.exceptions.custom_exceptions import PlaylistException



class PlaylistDetailsView(APIView):

    
    serializer_class = PlaylistInfoSerializer

    def _get_queryset(self):
       

        playlist_id = self.request.query_params.get("playlist_id", None)
        if not playlist_id:
            raise PlaylistException(
                item="Playlist Id", message="Please Provide Playlist Id."
            )
        playlist = Playlist.objects.get(id = playlist_id)
        return playlist

    def get(self, request):
       
        try:
            queryset = self._get_queryset()
            serialized_data = self.serializer_class(queryset).data

            return APIResponse(
                data=serialized_data,
                status_code=status.HTTP_200_OK,
                message="Fetched Playlist detail",
            )
        except settings.LAZY_EXCEPTIONS as ce:
            return APIResponse(
                status_code=ce.status_code,
                errors=ce.error_data(),
                message=ce.message,
                for_error=True,
            )
        except Exception as ce:
            return APIResponse(
                status_code=500,
                for_error=True,
                message=f"Unknown error occured in Playlist Details : {ce}",
            )


class CreatePlaylistAPIView(APIView):
     serializer_class = PlaylistSerializer
     playlist_info_serializer_class = PlaylistInfoSerializer
     def post(self, request):
        
        with transaction.atomic():
            data = request.data
           
            try:
                serializer_obj = self.serializer_class(data = data)
                if serializer_obj.is_valid():
                    playlist = Playlist.objects.create(title = data.get("title"))
                    tracks = Track.objects.filter(id__in=data.get("tracks"))
                    last_playlisttrack = PlaylistTrack.objects.filter(playlist=playlist).last()
                    if last_playlisttrack:
                        position = last_playlisttrack.position
                    else:
                        position = 1 
                    
                    for i in range(len(data.get("tracks"))):
                        playlisttrack = PlaylistTrack(playlist=playlist, track=tracks[i], position = position)
                        playlisttrack.save()    
                        position += 1
                    serialized_data = self.playlist_info_serializer_class(instance=playlist).data
                    return APIResponse(
                        data=serialized_data,
                        status_code=status.HTTP_200_OK,
                        message="Fetched Playlist detail",
                    )
            except settings.LAZY_EXCEPTIONS as ce:
                return APIResponse(
                    status_code=ce.status_code,
                    errors=ce.error_data(),
                    message=ce.message,
                    for_error=True,
                )
            except Exception as ce:
                return APIResponse(
                    status_code=500,
                    for_error=True,
                    message=f"Unknown error occured in Playlist Details : {ce}",
                )




class UpdatePlaylistAPIView(APIView):
    serializer_class = PlaylistSerializer
    playlist_info_serializer_class = PlaylistInfoSerializer

    def post(self, request):
        with transaction.atomic():
            data = request.data
            import pdb; pdb.set_trace()
            playlist_id = data.get("playlist_id")
            playlist = Playlist.objects.get(id = playlist_id)
            serializer_obj = self.serializer_class(instance=playlist, data = data)
            if serializer_obj.is_valid():
                playlist = serializer_obj.save()
                serialized_data = self.playlist_info_serializer_class(instance=playlist).data
                return APIResponse(
                        data=serialized_data,
                        status_code=status.HTTP_200_OK,
                        message="Fetched Playlist detail",
                    )
            try:
                pass
            except settings.LAZY_EXCEPTIONS as ce:
                return APIResponse(
                    status_code=ce.status_code,
                    errors=ce.error_data(),
                    message=ce.message,
                    for_error=True,
                )
            except Exception as ce:
                return APIResponse(
                    status_code=500,
                    for_error=True,
                    message=f"Unknown error occured in Playlist Details : {ce}",
                )



class PlaylistDeleteAPIView(APIView):
    def post(self, request):
        try:
            
            playlist_id = request.data.get("playlist_id", None)
            if not playlist_id:
                raise PlaylistException(
                    item="Playlist Id", message="Please Provide Playlist Id."
                )
            playlist = Playlist.objects.get(id = playlist_id)
            playlist.delete()
            return APIResponse(
              
                status_code=status.HTTP_200_OK,
                message="playlist deleted",
            )
        except settings.LAZY_EXCEPTIONS as ce:
            return APIResponse(
                status_code=ce.status_code,
                errors=ce.error_data(),
                message=ce.message,
                for_error=True,
            )
        except Exception as ce:
            return APIResponse(
                status_code=500,
                for_error=True,
                message=f"Unknown error occured in playlist Details : {ce}",
            )