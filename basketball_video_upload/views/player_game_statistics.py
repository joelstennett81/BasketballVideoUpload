from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from basketball_video_upload.models import PlayerGameStatistic
from basketball_video_upload.forms import PlayerForm, PlayerGameStatisticForm


class PlayerGameStatisticListView(View):
    def get(self, request):
        playerGameStatistics = PlayerGameStatistic.objects.all()
        return render(request, 'player_game_statistics/list_player_game_statistics.html',
                      {'playerGameStatistics': playerGameStatistics})


class PlayerGameStatisticCreateView(CreateView):
    model = PlayerGameStatistic
    form_class = PlayerGameStatisticForm
    template_name = 'player_game_statistics/new_player_game_statistic.html'
