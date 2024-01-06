from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from basketball_video_upload.models import Game, Season, PlayerGameHighlightVideo, PlayerGameStatistic, \
    PlayerSeasonStatistic, Profile
from basketball_video_upload.forms import GameForm, SeasonForm, PlayerGameHighlightVideoForm, \
    PlayerGameStatisticForm, PlayerSeasonStatisticForm, AdminProfileForm, PlayerProfileForm


def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('basketball_video_upload:login')


def register(request):
    admin_form = None
    player_form = None
    if request.method == "POST":
        user_type = request.POST.get('user_type')
        user_form = UserCreationForm(request.POST)
        profile_form = None

        if user_type == 'administrator':
            profile_form = AdminProfileForm(request.POST)
        elif user_type == 'player':
            profile_form = PlayerProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            if user_type == 'administrator':
                profile.is_administrator = True
                profile.is_player = False
            else:
                profile.is_player = True
                profile.is_administrator = False
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('basketball_video_upload:login')
    else:
        user_form = UserCreationForm()
        user_type = request.GET.get('user_type', 'player')  # Default to 'player' if no user_type is provided
        admin_form = AdminProfileForm()
        player_form = PlayerProfileForm()

    return render(request, 'registration/register.html',
                  {'user_form': user_form, 'admin_form': admin_form, 'player_form': player_form,
                   'user_type': user_type})


class PlayerListView(View):
    def get(self, request):
        players = Profile.objects.all()
        return render(request, 'players/list_personal_info.html',
                      {'players': players})


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
