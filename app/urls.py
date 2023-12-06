from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from basketball_video_upload.views import registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', registration.register, name='register'),
]
