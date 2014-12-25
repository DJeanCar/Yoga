import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = ')(lbipuf=amwpdn5n!%f@na%i#=_#e@2x+h68!1((q^ru_bti$'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users',
    'apps.classes',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'yoga.urls'
WSGI_APPLICATION = 'yoga.wsgi.application'


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
        'apps.users.backends.EmailAuthentication',
    )

PAYPAL_RECEIVER_EMAIL = "mjeanc.104@gmail.com"

PAYPAL_MODE = 'live'  # sandbox or live
PAYPAL_CLIENT_ID = 'AXEx3BC50ISgT0RAtwDWNGTmKt-EHwmhbt6ADpbGRE96eJc4ZLByPHwNVtvf'
PAYPAL_CLIENT_SECRET = 'EL6cPhDXwO2tIs1Cvit35gNyC3NTCrQue67J6QdG24L17JIlOBLsRqyeiL4s'


