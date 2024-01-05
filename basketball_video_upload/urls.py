from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from basketball_video_upload.views import views

app_name = 'basketball_video_upload'

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('players/', views.PlayerListView.as_view(), name='list_players'),
    path('players/new/', views.PlayerCreateView.as_view(), name='create_player'),
    path('games/', views.GameListView.as_view(), name='list_games'),
    path('games/new/', views.GameCreateView.as_view(), name='create_game'),
    path('seasons/', views.SeasonListView.as_view(), name='list_seasons'),
    path('seasons/new/', views.SeasonCreateView.as_view(), name='create_season'),
    path('player_game_highlight_videos/', views.PlayerGameHighlightVideoListView.as_view(),
         name='list_player_game_highlight_videos'),
    path('player_game_highlight_videos/new/', views.PlayerGameHighlightVideoCreateView.as_view(),
         name='create_player_game_highlight_video'),
    path('player_game_statistics/', views.PlayerGameStatisticListView.as_view(), name='list_player_game_statistics'),
    path('player_game_statistics/new/', views.PlayerGameStatisticCreateView.as_view(),
         name='create_player_game_statistic'),
    path('player_season_statistics/', views.PlayerSeasonStatisticListView.as_view(),
         name='list_player_season_statistics'),
    path('player_season_statistics/new/', views.PlayerSeasonStatisticCreateView.as_view(),
         name='create_player_season_statistic'),
]
