from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from basketball_video_upload.views import views

app_name = 'basketball_video_upload'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('show_profile/', views.ProfileView.as_view(), name='show_profile'),
    path('list_all_players/', views.PlayerListView.as_view(), name='list_all_players'),
    path('list_all_player_game_highlight_videos/', views.AllPlayerGameHighlightVideoListView.as_view(),
         name='list_all_player_game_highlight_videos'),
    path('list_personal_player_game_highlight_videos/', views.PersonalPlayerGameHighlightVideoListView.as_view(),
         name='list_personal_player_game_highlight_videos'),
    path('view_individual_player_game_highlight_video/<int:video_id>/',
         views.IndividualPlayerHighlightVideoView.as_view(),
         name='view_individual_player_highlight_video'),
    path('player_game_highlight_videos/new/', views.PlayerGameHighlightVideoCreateView.as_view(),
         name='create_player_game_highlight_video'),
    path('admin/', admin.site.urls),
]
