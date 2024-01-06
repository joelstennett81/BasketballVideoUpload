from django.db.models import Sum
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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


class Game(models.Model):
    season = models.ForeignKey('Season', on_delete=models.CASCADE, null=True)
    date = models.DateField(default=timezone.now, null=True)
    team_one = models.CharField(max_length=100, null=True)
    team_two = models.CharField(max_length=100, null=True)


class Season(models.Model):
    season_type = models.CharField(max_length=5, choices=[('AAU', 'AAU'), ('HS', 'High School')], null=True)
    season_start_date = models.DateField(null=True, blank=True)
    season_end_date = models.DateField(null=True, blank=True)


class PlayerGameHighlightVideo(models.Model):
    player = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    video = models.FileField(upload_to='player_game_highlights/', null=True)
    video_name = models.CharField(max_length=100, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)


class PlayerGameStatistic(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    player = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    points = models.PositiveIntegerField(default=0, null=True)
    rebounds = models.PositiveIntegerField(default=0, null=True)
    assists = models.PositiveIntegerField(default=0, null=True)
    turnovers = models.PositiveIntegerField(default=0, null=True)
    blocks = models.PositiveIntegerField(default=0, null=True)
    steals = models.PositiveIntegerField(default=0, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        player_season_statistic, created = PlayerSeasonStatistic.objects.get_or_create(player=self.player,
                                                                                       season=self.game.season)
        player_season_statistic.total_points = \
            PlayerGameStatistic.objects.filter(player=self.player, season=self.game.season).aggregate(Sum('points'))[
                'points__sum'] or 0
        player_season_statistic.total_rebounds = \
            PlayerGameStatistic.objects.filter(player=self.player, season=self.game.season).aggregate(Sum('rebounds'))[
                'rebounds__sum'] or 0
        player_season_statistic.total_assists = \
            PlayerGameStatistic.objects.filter(player=self.player, season=self.game.season).aggregate(Sum('assists'))[
                'assists__sum'] or 0
        player_season_statistic.total_turnovers = \
            PlayerGameStatistic.objects.filter(player=self.player, season=self.game.season).aggregate(Sum('turnovers'))[
                'turnovers__sum'] or 0
        player_season_statistic.total_blocks = \
            PlayerGameStatistic.objects.filter(player=self.player, season=self.game.season).aggregate(Sum('blocks'))


class PlayerSeasonStatistic(models.Model):
    player = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
    total_points = models.PositiveIntegerField(default=0, null=True)
    total_rebounds = models.PositiveIntegerField(default=0, null=True)
    total_assists = models.PositiveIntegerField(default=0, null=True)
    total_turnovers = models.PositiveIntegerField(default=0, null=True)
    total_blocks = models.PositiveIntegerField(default=0, null=True)
    total_steals = models.PositiveIntegerField(default=0, null=True)
    games_played = models.PositiveIntegerField(default=0, null=True)
