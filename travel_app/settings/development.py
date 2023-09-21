import os
from decouple import config
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True
# DEBUG = config('DEBUG', cast=bool)

CREATE_APPS = [
    'apps.travel',
    'apps.advertising',
    'apps.travel_service',
    'apps.users',
    'apps.favorite',
]
INSTALLED_LIBRARY = [
    'django_filters',
    'jazzmin',
    'rest_framework',
    'drf_yasg',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    "corsheaders",
    'phonenumbers',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
INSTALLED_APPS = INSTALLED_LIBRARY + CREATE_APPS + DJANGO_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
from .base import *
