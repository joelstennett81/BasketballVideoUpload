from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from basketball_video_upload.decorators import admin_or_coach_required
from basketball_video_upload.models import Profile, PlayerGameHighlightVideo, PlayerGameStatistic


@method_decorator(admin_or_coach_required, name='get')
class PlayerListView(View):
    def get(self, request):
        players = Profile.objects.filter(is_player=True)
        return render(request, 'coaches_and_admins/list_all_players.html',
                      {'players': players})


@method_decorator(admin_or_coach_required, name='get')
class AllPlayerGameHighlightVideoListView(View):
    def get(self, request):
        playerGameHighlightVideos = PlayerGameHighlightVideo.objects.all()
        return render(request,
                      'coaches_and_admins/list_all_player_game_highlight_videos.html',
                      {'videos': playerGameHighlightVideos})


@method_decorator(admin_or_coach_required, name='get')
class AllPlayerGameStatisticListView(View):
    def get(self, request):
        playerGameStatistics = PlayerGameStatistic.objects.all()
        return render(request, 'players/player_game_statistics/list_personal_player_game_statistics.html',
                      {'playerGameStatistics': playerGameStatistics})
