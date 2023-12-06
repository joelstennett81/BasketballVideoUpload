from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from basketball_video_upload.models import Season
from basketball_video_upload.forms import SeasonForm


class SeasonListView(View):
    def get(self, request):
        seasons = Season.objects.all()
        return render(request, 'seasons/list_seasons.html',
                      {'seasons': seasons})


class SeasonCreateView(CreateView):
    model = Season
    form_class = SeasonForm
    template_name = 'seasons/new_season.html'
