# Generated by Django 5.0 on 2024-01-06 04:00

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('team_one', models.CharField(max_length=100, null=True)),
                ('team_two', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_type', models.CharField(choices=[('AAU', 'AAU'), ('HS', 'High School')], max_length=5, null=True)),
                ('season_start_date', models.DateField(blank=True, null=True)),
                ('season_end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('team_coaching', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('height_feet', models.PositiveIntegerField(null=True, verbose_name=[django.core.validators.MinValueValidator(4), django.core.validators.MaxValueValidator(8)])),
                ('height_inches', models.PositiveIntegerField(null=True, verbose_name=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(11)])),
                ('weight_in_lbs', models.PositiveIntegerField(null=True, verbose_name=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(450)])),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('aau_team_name', models.CharField(max_length=100, null=True)),
                ('high_school_team_name', models.CharField(max_length=100, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('high_school_graduation_year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2099)])),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGameHighlightVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='player_game_highlights/')),
                ('video_name', models.CharField(max_length=100, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basketball_video_upload.game')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basketball_video_upload.player')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGameStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField(default=0, null=True)),
                ('rebounds', models.PositiveIntegerField(default=0, null=True)),
                ('assists', models.PositiveIntegerField(default=0, null=True)),
                ('turnovers', models.PositiveIntegerField(default=0, null=True)),
                ('blocks', models.PositiveIntegerField(default=0, null=True)),
                ('steals', models.PositiveIntegerField(default=0, null=True)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basketball_video_upload.game')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basketball_video_upload.player')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerSeasonStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_points', models.PositiveIntegerField(default=0, null=True)),
                ('total_rebounds', models.PositiveIntegerField(default=0, null=True)),
                ('total_assists', models.PositiveIntegerField(default=0, null=True)),
                ('total_turnovers', models.PositiveIntegerField(default=0, null=True)),
                ('total_blocks', models.PositiveIntegerField(default=0, null=True)),
                ('total_steals', models.PositiveIntegerField(default=0, null=True)),
                ('games_played', models.PositiveIntegerField(default=0, null=True)),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basketball_video_upload.player')),
                ('season', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basketball_video_upload.season')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basketball_video_upload.season'),
        ),
    ]
