from django.core.files.storage import default_storage

from .models import Profile, PlayerGameHighlightVideo
from django import forms
import os


class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date']


class PlayerProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'height_feet', 'height_inches', 'weight_in_lbs', 'city',
                  'state', 'aau_team_name', 'high_school_team_name', 'high_school_graduation_year']


def validate_video(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.avi', '.mov', '.flv', '.wmv']
    if not ext.lower() in valid_extensions:
        raise forms.ValidationError('Unsupported file extension.')


class PlayerGameHighlightVideoForm(forms.ModelForm):
    video = forms.FileField(validators=[validate_video])

    class Meta:
        model = PlayerGameHighlightVideo
        fields = ['video_name', 'game_date', 'team_playing_for', 'team_playing_against']
