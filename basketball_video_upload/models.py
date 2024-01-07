from django.core.files.storage import default_storage
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_administrator = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    birth_date = models.DateField(null=True, blank=True)
    height_feet = models.PositiveIntegerField(null=True, blank=True)
    height_inches = models.PositiveIntegerField(null=True, blank=True)
    weight_in_lbs = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    aau_team_name = models.CharField(max_length=100, null=True, blank=True)
    high_school_team_name = models.CharField(max_length=100, null=True, blank=True)
    high_school_graduation_year = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.user = kwargs.pop('user', None) or self.user
        super().save(*args, **kwargs)


class PlayerGameHighlightVideo(models.Model):
    player = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    video_name = models.CharField(max_length=100, null=True)
    s3_object_name = models.CharField(max_length=1000, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    game_date = models.DateField(null=True)
    team_playing_for = models.CharField(max_length=100,null=True)
    team_playing_against = models.CharField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        self.video_name = self.video_name.replace(" ", "_")
        print('self.video_name: ', self.video_name)
        self.s3_object_name = f'{self.player.first_name}_{self.player.last_name}/{self.video_name.replace(" ", "_")}'
        print('self.s3_object: ', self.s3_object_name)
        super().save(*args, **kwargs)
