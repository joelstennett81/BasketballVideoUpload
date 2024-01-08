# Generated by Django 5.0 on 2024-01-08 05:49

import django.db.models.deletion
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
                ('date', models.DateField(blank=True, null=True)),
                ('type', models.CharField(choices=[('AAU', 'AAU'), ('HS', 'High School')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_administrator', models.BooleanField(default=False)),
                ('is_player', models.BooleanField(default=False)),
                ('is_coach', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email_address', models.EmailField(max_length=254, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('height_feet', models.PositiveIntegerField(blank=True, null=True)),
                ('height_inches', models.PositiveIntegerField(blank=True, null=True)),
                ('weight_in_lbs', models.PositiveIntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('aau_team_name', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_team_name', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_graduation_year', models.IntegerField(blank=True, null=True)),
                ('team_coaching', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGameStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField(default=0)),
                ('rebounds', models.PositiveIntegerField(default=0)),
                ('assists', models.PositiveIntegerField(default=0)),
                ('turnovers', models.PositiveIntegerField(default=0)),
                ('blocks', models.PositiveIntegerField(default=0)),
                ('steals', models.PositiveIntegerField(default=0)),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basketball_video_upload.game')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basketball_video_upload.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGameHighlightVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=100, null=True)),
                ('s3_object_name', models.CharField(max_length=1000, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('team_playing_for', models.CharField(max_length=100, null=True)),
                ('team_playing_against', models.CharField(max_length=100, null=True)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basketball_video_upload.game')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basketball_video_upload.profile')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basketball_video_upload.profile'),
        ),
    ]
