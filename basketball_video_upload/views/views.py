from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from basketball_video_upload.models import Player, Game, Season, PlayerGameHighlightVideo, PlayerGameStatistic, \
    PlayerSeasonStatistic
from basketball_video_upload.forms import PlayerForm, GameForm, SeasonForm, PlayerGameHighlightVideoForm, \
    PlayerGameStatisticForm, PlayerSeasonStatisticForm


def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('basketball_video_upload:login')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class PlayerListView(View):
    def get(self, request):
        players = Player.objects.all()
        return render(request, 'players/list_players.html',
                      {'players': players})


class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/new_player.html'


class GameListView(View):
    def get(self, request):
        games = Game.objects.all()
        return render(request, 'games/list_games.html',
                      {'games': games})


class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'games/new_game.html'


class SeasonListView(View):
    def get(self, request):
        seasons = Season.objects.all()
        return render(request, 'seasons/list_seasons.html',
                      {'seasons': seasons})


class SeasonCreateView(CreateView):
    model = Season
    form_class = SeasonForm
    template_name = 'seasons/new_season.html'


class PlayerGameHighlightVideoListView(View):
    def get(self, request):
        playerGameHighlightVideos = PlayerGameHighlightVideo.objects.all()
        return render(request, 'player_game_highlight_videos/list_player_game_highlight_videos.html',
                      {'playerGameHighlightVideo': playerGameHighlightVideos})


class PlayerGameHighlightVideoCreateView(CreateView):
    model = PlayerGameHighlightVideo
    form_class = PlayerGameHighlightVideoForm
    template_name = 'player_game_highlight_videos/new_player_game_highlight_videos.html'


class PlayerGameStatisticListView(View):
    def get(self, request):
        playerGameStatistics = PlayerGameStatistic.objects.all()
        return render(request, 'player_game_statistics/list_player_game_statistics.html',
                      {'playerGameStatistics': playerGameStatistics})


class PlayerGameStatisticCreateView(CreateView):
    model = PlayerGameStatistic
    form_class = PlayerGameStatisticForm
    template_name = 'player_game_statistics/new_player_game_statistic.html'


class PlayerSeasonStatisticListView(View):
    def get(self, request):
        playerSeasonStatistics = PlayerSeasonStatistic.objects.all()
        return render(request, 'player_season_statistics/list_player_season_statistics.html',
                      {'playerSeasonStatistics': playerSeasonStatistics})


class PlayerSeasonStatisticCreateView(CreateView):
    model = PlayerSeasonStatistic
    form_class = PlayerSeasonStatisticForm
    template_name = 'player_season_statistics/new_player_season_statistic.html'
