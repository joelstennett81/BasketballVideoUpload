from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from basketball_video_upload.models import PlayerGameHighlightVideo, Profile
from basketball_video_upload.forms import PlayerGameHighlightVideoForm, AdminProfileForm, PlayerProfileForm


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


class ProfileView(View):
    def get(self, request):
        player = request.user.profile
        return render(request, 'players/profile.html',
                      {'player': player})


class PlayerListView(View):
    def get(self, request):
        players = Profile.objects.all()
        return render(request, 'players/list_all_players.html',
                      {'players': players})


class AllPlayerGameHighlightVideoListView(View):
    def get(self, request):
        playerGameHighlightVideos = PlayerGameHighlightVideo.objects.all()
        return render(request, 'player_game_highlight_videos/list_all_player_game_highlight_videos.html',
                      {'playerGameHighlightVideos': playerGameHighlightVideos})


class PersonalPlayerGameHighlightVideoListView(View):
    def get(self, request):
        playerGameHighlightVideos = PlayerGameHighlightVideo.objects.filter(player=request.user.profile)
        print('player game videos: ', playerGameHighlightVideos)
        return render(request, 'player_game_highlight_videos/list_personal_player_game_highlight_videos.html',
                      {'playerGameHighlightVideos': playerGameHighlightVideos})


class PlayerGameHighlightVideoCreateView(CreateView):
    model = PlayerGameHighlightVideo
    form_class = PlayerGameHighlightVideoForm
    template_name = 'player_game_highlight_videos/new_player_game_highlight_videos.html'
    success_url = '/list_personal_player_game_highlight_videos/'

    def form_valid(self, form):
        form.instance.player = self.request.user.profile
        return super().form_valid(form)
