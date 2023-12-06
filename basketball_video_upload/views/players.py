from django.shortcuts import render, redirect
from django.views import View
from basketball_video_upload.models import Player
from basketball_video_upload.forms import PlayerForm


class PlayerListView(View):
    def get(self, request):
        players = Player.objects.all()
        return render(request, 'players/players.html', {'players': players})

    def post(self, request):
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('players')
        return render(request, 'players/players.html', {'form': form})
