from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView

from basketball_video_upload.decorators import player_required
from basketball_video_upload.forms import PlayerGameHighlightVideoForm
from basketball_video_upload.models import PlayerGameHighlightVideo
from basketball_video_upload.views.s3 import get_url_for_video, upload_video_to_s3


@method_decorator(player_required, name='get')
class ProfileView(View):
    def get(self, request):
        player = request.user.profile
        return render(request, 'players/profile.html',
                      {'player': player})


@method_decorator(player_required, name='get')
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
        return render(request, 'players/player_game_highlight_videos/list_personal_player_game_highlight_videos.html',
                      {'videos': videos})


@method_decorator(player_required, name='get')
class IndividualPlayerHighlightVideoView(View):
    def get(self, request, video_id):
        print('video id: ', video_id)
        video = get_object_or_404(PlayerGameHighlightVideo, id=video_id, player=request.user.profile)
        video_url = get_url_for_video(request, video.video_name)
        print('final video url: ', video_url)
        return render(request, 'players/player_game_highlight_videos/individual_player_highlight_video.html',
                      {'video': video, 'video_url': video_url})


@method_decorator(player_required, name='get')
class PlayerGameHighlightVideoCreateView(CreateView):
    model = PlayerGameHighlightVideo
    form_class = PlayerGameHighlightVideoForm
    template_name = 'players/player_game_highlight_videos/new_player_game_highlight_videos.html'
    success_url = '/list_personal_player_game_highlight_videos/'

    def form_valid(self, form):
        form.instance.player = self.request.user.profile
        form.instance.s3_object_name = f'{form.instance.player.first_name}_{form.instance.player.last_name}/{form.instance.video_name}'
        video_name = form.instance.video_name.replace(" ", "_")
        upload_video_to_s3(self.request, form.cleaned_data["video"], video_name)
        return super().form_valid(form)



