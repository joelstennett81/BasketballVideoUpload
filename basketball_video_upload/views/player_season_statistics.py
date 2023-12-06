from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from basketball_video_upload.models import PlayerSeasonStatistic
from basketball_video_upload.forms import PlayerSeasonStatisticForm


class PlayerSeasonStatisticListView(View):
    def get(self, request):
        playerSeasonStatistics = PlayerSeasonStatistic.objects.all()
        return render(request, 'player_season_statistics/list_player_season_statistics.html',
                      {'playerSeasonStatistics': playerSeasonStatistics})


class PlayerSeasonStatisticCreateView(CreateView):
    model = PlayerSeasonStatistic
    form_class = PlayerSeasonStatisticForm
    template_name = 'player_season_statistics/new_player_season_statistic.html'
