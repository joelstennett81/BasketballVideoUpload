from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from basketball_video_upload.decorators import admin_required
from basketball_video_upload.models import Profile, PlayerGameHighlightVideo


@method_decorator(admin_required, name='get')
class PlayerListView(View):
    def get(self, request):
        players = Profile.objects.all()
        return render(request, 'admins/list_all_players.html',
                      {'players': players})


@method_decorator(admin_required, name='get')
class AllPlayerGameHighlightVideoListView(View):
    def get(self, request):
        playerGameHighlightVideos = PlayerGameHighlightVideo.objects.all()
        return render(request,
                      'admins/list_all_player_game_highlight_videos.html',
                      {'videos': playerGameHighlightVideos})
