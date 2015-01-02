from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Series',
        'USER': 'cineuserprod',
        'PASSWORD': 'cine',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = 'http://seriesparatodos.com/static/'
MEDIA_URL = 'http://seriesparatodos.com/media/'
STATIC_ROOT = BASE_DIR.child('static')
MEDIA_ROOT = BASE_DIR.child('media')
