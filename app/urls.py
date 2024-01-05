from django.urls import include, path

urlpatterns = [
   # your other URL patterns go here
   path('', include('basketball_video_upload.urls')),
]


