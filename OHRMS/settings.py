
from pathlib import Path
import dj_database_url
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-0)zsyrk(i8nc67lrmlw=qzqa2nlf(ka+61c-o9g@9!)dv=&taj'

DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
   
]

ROOT_URLCONF = 'OHRMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'OHRMS.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'OHRMS',
#         'USER': 'postgres',
#         'PASSWORD': 'a/ur14623/10',
#         'HOST': 'localhost',  # If running on localhost, use 'localhost' or '127.0.0.1'
#         'PORT': '5432',  # Use the default PostgreSQL port (5432) unless you've configured a different one
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ohrmsdb',
        'USER': 'ohrmsdb_user',
        'PASSWORD': 'rYCzLOMytQXtRhQ0rAneqbXUa3XptJR4',
        'HOST': 'dpg-cljnhe98mmjc73da4kj0-a.oregon-postgres.render.com',
        'PORT': '',
    }
}
database_url = "postgres://ohrmsdb_user:rYCzLOMytQXtRhQ0rAneqbXUa3XptJR4@dpg-cljnhe98mmjc73da4kj0-a/ohrmsdb"

parsed_db = dj_database_url.parse(database_url)

DATABASES['default'].update(parsed_db)


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / "static"] # new
STATIC_ROOT = BASE_DIR / "staticfiles" # new

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
