from .models import Profile, PlayerGameHighlightVideo, PlayerGameStatistic, Game
from django import forms
import os


class UserTypeForm(forms.Form):
    user_type = forms.ChoiceField(
        choices=[('administrator', 'Administrator'), ('player', 'Player'), ('coach', 'Coach')])


class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email_address']


class CoachProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email_address', 'team_coaching']


class PlayerProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email_address', 'height_feet', 'height_inches', 'weight_in_lbs', 'city',
                  'state', 'aau_team_name', 'high_school_team_name', 'high_school_graduation_year']


def validate_video(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.avi', '.mov', '.flv', '.wmv']
    if not ext.lower() in valid_extensions:
        raise forms.ValidationError('Unsupported file extension.')


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['date']


class PlayerGameHighlightVideoForm(forms.ModelForm):
    video = forms.FileField(validators=[validate_video])

    class Meta:
        model = PlayerGameHighlightVideo
        fields = ['video_name', 'team_playing_for', 'team_playing_against']


class PlayerGameStatisticForm(forms.ModelForm):
    class Meta:
        model = PlayerGameStatistic
        fields = ['points', 'rebounds', 'assists', 'turnovers', 'blocks', 'steals']
