from .models import Profile, PlayerGameStatistic, Season, PlayerSeasonStatistic, PlayerGameHighlightVideo, Game
from django import forms


class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date']


class PlayerProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'height_feet', 'height_inches', 'weight_in_lbs', 'city',
                  'state', 'aau_team_name', 'high_school_team_name', 'high_school_graduation_year']


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
