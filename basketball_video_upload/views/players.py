from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from basketball_video_upload.models import Player
from basketball_video_upload.forms import PlayerForm


class PlayerListView(View):
    def get(self, request):
        players = Player.objects.all()
        return render(request, 'players/list_players.html',
                      {'players': players})


class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/new_player.html'
