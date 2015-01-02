from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Yoga',
        'USER': 'yogauser',
        'PASSWORD': 'yoga',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = 'http://104.131.185.89/static2/'
MEDIA_URL = 'http://104.131.185.89/media/'
STATIC_ROOT = BASE_DIR.child('static2')
MEDIA_ROOT = BASE_DIR.child('media')
