from .settings import *

DEBUG = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'basketball-video-upload-production',
       'USER': 'postgres',
       'PASSWORD': 'admin',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}
