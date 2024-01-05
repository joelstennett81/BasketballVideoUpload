from django import forms
from .models import Player, PlayerGameStatistic, Season, PlayerSeasonStatistic, PlayerGameHighlightVideo, Game


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'height', 'weight', 'aau_team_name', 'high_school_team_name', 'birth_date',
                  'high_school_graduation_year']


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['season', 'date', 'team_one', 'team_two']


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['season_type', 'season_start_date', 'season_end_date']


class PlayerGameHighlightVideoForm(forms.ModelForm):
    class Meta:
        model = PlayerGameHighlightVideo
        fields = ['player', 'game', 'video', 'video_name']


class PlayerGameStatisticForm(forms.ModelForm):
    class Meta:
        model = PlayerGameStatistic
        fields = ['game', 'player', 'points', 'rebounds', 'assists', 'turnovers', 'blocks', 'steals']


class PlayerSeasonStatisticForm(forms.ModelForm):
    class Meta:
        model = PlayerSeasonStatistic
        fields = ['player', 'season', 'total_points', 'total_rebounds', 'total_assists', 'total_turnovers',
                  'total_blocks', 'total_steals', 'games_played']
