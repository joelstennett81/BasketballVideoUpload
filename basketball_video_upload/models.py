from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    height = models.PositiveIntegerField([MinValueValidator(48), MaxValueValidator(96)])
    weight = models.PositiveIntegerField([MinValueValidator(50), MaxValueValidator(450)])
    aau_team_name = models.CharField(max_length=100, null=True)
    high_school_team_name = models.CharField(max_length=100, null=True)
    birth_date = models.DateField(null=True, blank=True)
    high_school_graduation_year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)])

    def save(self, *args, **kwargs):
        self.user = kwargs.pop('user', None) or self.user
        super().save(*args, **kwargs)


class Season(models.Model):
    season_type = models.CharField(max_length=5, choices=[('AAU', 'AAU'), ('HS', 'High School')])
    season_start_date = models.DateField(null=True, blank=True)
    season_end_date = models.DateField(null=True, blank=True)


class PlayerGameStatistic(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game_date = models.DateField(default=timezone.now)
    team_playing_against = models.CharField(max_length=100)
    points = models.PositiveIntegerField(default=0)
    rebounds = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    turnovers = models.PositiveIntegerField(default=0)
    blocks = models.PositiveIntegerField(default=0)
    steals = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        player_season_statistic, created = PlayerSeasonStatistic.objects.get_or_create(player=self.player,
                                                                                       season=self.season)
        player_season_statistic.total_points = \
            PlayerGameStatistic.objects.filter(player=self.player, season=self.season).aggregate(Sum('points'))[
                'points__sum'] or 0
        player_season_statistic.total_rebounds = \
            PlayerGameStatistic.objects.filter(player=self.player, season=self.season).aggregate(Sum('rebounds'))[
                'rebounds__sum'] or 0
        player_season_statistic.total_assists = \
            PlayerGameStatistic.objects.filter(player=self.player, season=self.season).aggregate(Sum('assists'))[
                'assists__sum'] or 0
        player_season_statistic.total_turnovers = \
            PlayerGameStatistic.objects.filter(player=self.player, season=self.season).aggregate(Sum('turnovers'))[
                'turnovers__sum'] or 0
        player_season_statistic.total_blocks = \
            PlayerGameStatistic.objects.filter(player=self.player, season=self.season).aggregate(Sum('blocks'))[
                'blocks__sum'] or 0
        player_season_statistic.total_steals = \
            PlayerGameStatistic.objects.filter(player=self.player, season=self.season).aggregate(Sum('steals'))[
                'steals__sum'] or 0
        player_season_statistic.save()


class PlayerSeasonStatistic(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    total_points = models.PositiveIntegerField(default=0)
    total_rebounds = models.PositiveIntegerField(default=0)
    total_assists = models.PositiveIntegerField(default=0)
    total_turnovers = models.PositiveIntegerField(default=0)
    total_blocks = models.PositiveIntegerField(default=0)
    total_steals = models.PositiveIntegerField(default=0)
    games_played = models.PositiveIntegerField(default=0)
