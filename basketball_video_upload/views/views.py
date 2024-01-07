import boto3
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView
from django.conf import settings

from basketball_video_upload.models import PlayerGameHighlightVideo, Profile
from basketball_video_upload.forms import PlayerGameHighlightVideoForm, AdminProfileForm, PlayerProfileForm


def home(request):
    print('in home')
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
            print('user errirs: ', user_form.errors)
            print('login error')
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
        videos = []
        for video in playerGameHighlightVideos:
            video_url = get_url_for_video(request, video.video_name)
            videos.append({
                'id': video.id,
                'player': video.player,
                'game_date': video.game_date,
                'video_url': video_url,
                'video_name': video.video_name,
                'uploaded_at': video.uploaded_at,
            })
        return render(request, 'player_game_highlight_videos/list_personal_player_game_highlight_videos.html',
                      {'videos': videos})


class IndividualPlayerHighlightVideoView(View):
    def get(self, request, video_id):
        video = get_object_or_404(PlayerGameHighlightVideo, id=video_id, player=request.user.profile)
        video_url = get_url_for_video(request, video.video_name)
        return render(request, 'player_game_highlight_videos/individual_player_highlight_video.html',
                      {'video': video, 'video_url': video_url})


class PlayerGameHighlightVideoCreateView(CreateView):
    model = PlayerGameHighlightVideo
    form_class = PlayerGameHighlightVideoForm
    template_name = 'player_game_highlight_videos/new_player_game_highlight_videos.html'
    success_url = '/list_personal_player_game_highlight_videos/'

    def form_valid(self, form):
        form.instance.player = self.request.user.profile
        form.instance.s3_object_name = f'{form.instance.player.first_name}_{form.instance.player.last_name}/{form.instance.video_name}'
        upload_video_to_s3(self.request, form.cleaned_data["video"], form.instance.video_name)
        return super().form_valid(form)


def upload_video_to_s3(request, file, video_name):
    s3 = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    key = f'{request.user.profile.first_name}_{request.user.profile.last_name}/{video_name}'
    print()
    s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME).put_object(Key=key, Body=file)


def get_url_for_video(request, video_name):
    s3 = boto3.client('s3')
    params = {
        'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
        'Key': str(video_name),
    }
    print('key: ', str(video_name))
    url = 'https://' + settings.AWS_STORAGE_BUCKET_NAME + '.s3.us-east-2.amazonaws.com/' + request.user.profile.first_name + '_' + request.user.profile.last_name + '/' + video_name
    return url


def get_presigned_url_for_video(request, object_name):
    s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    params = {
        'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
        'Key': str(object_name),
    }
    response = s3.generate_presigned_url('get_object', Params=params, ExpiresIn=3600)
    return response
