from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from basketball_video_upload.views import misc, players, coaches_and_admins, games

app_name = 'basketball_video_upload'

urlpatterns = [
    path('', misc.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', misc.logout_view, name='logout'),
    path('register/', misc.register, name='register'),
    path('choose_role/', misc.choose_role, name='choose_role'),
    path('upload_profile/', misc.upload_profile, name='upload_profile'),
    path('show_profile/', players.ProfileView.as_view(), name='show_profile'),
    path('games/new/', games.GameCreateView.as_view(), name='create_game'),
    path('list_all_games/', games.AllGameListView.as_view(), name='list_all_games'),
    path('list_personal_games/', games.PersonalGameListView.as_view(), name='list_personal_games'),
    path('list_all_players/', coaches_and_admins.PlayerListView.as_view(), name='list_all_players'),
    path('list_all_player_game_highlight_videos/', coaches_and_admins.AllPlayerGameHighlightVideoListView.as_view(),
         name='list_all_player_game_highlight_videos'),
    path('list_personal_player_game_highlight_videos/', players.PersonalPlayerGameHighlightVideoListView.as_view(),
         name='list_personal_player_game_highlight_videos'),
    path('view_individual_player_game_highlight_video/<int:video_id>/',
         players.IndividualPlayerHighlightVideoView.as_view(),
         name='view_individual_player_game_highlight_video'),
    path('player_game_highlight_videos/new/<int:id>', players.PlayerGameHighlightVideoCreateView.as_view(),
         name='create_player_game_highlight_video'),
    path('list_all_player_game_statistics/', coaches_and_admins.AllPlayerGameStatisticListView.as_view(),
         name='list_all_player_game_statistics'),
    path('list_personal_player_game_statistics/', players.PersonalPlayerGameStatisticListView.as_view(),
         name='list_personal_player_game_statistics'),
    path('view_individual_player_game_statistic/<int:game_id>/',
         players.IndividualPlayerGameStatisticView.as_view(),
         name='view_individual_player_statistic'),
    path('player_game_statistics/new/<int:id>', players.PlayerGameStatisticCreateView.as_view(),
         name='create_player_game_statistic'),
    path('admin/', admin.site.urls),
]
