from django.db.models import Count
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView

from basketball_video_upload.decorators import player_required
from basketball_video_upload.forms import GameForm
from basketball_video_upload.models import Game
from basketball_video_upload.views.s3 import upload_video_to_s3


@method_decorator(player_required, name='get')
class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'games/new_game.html'
    success_url = '/list_personal_games/'

    def form_valid(self, form):
        form.instance.player = self.request.user.profile
        return super().form_valid(form)


@method_decorator(player_required, name='get')
class AllGameListView(View):
    def get(self, request):
        games = Game.objects.all()
        return render(request, 'games/list_all_games.html',
                      {'games': games})


@method_decorator(player_required, name='get')
class PersonalGameListView(View):
    def get(self, request):
        games = Game.objects.filter(player=request.user.profile).annotate(
            has_highlight=Count('playergamehighlightvideo__game'),
            has_statistic=Count('playergamestatistic__game')
        )
        return render(request, 'games/list_personal_games.html',
                      {'games': games})
