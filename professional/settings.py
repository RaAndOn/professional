"""
Django settings for professional project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
# from settings_secret import *
import dj_database_url
import professional

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

secret_path = os.path.join(os.path.dirname(professional.__file__), 'settings_secret.py')
secret = os.path.isfile(secret_path)

if secret:
  from settings_secret import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if not secret:
  SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['joshua-raanan-professional.herokuapp.com','joshua-raanan.com', 'www.joshua-raanan.com', 'localhost']


# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'flatblocks',
  'jquery',
  'website',
  'reversion',
  'tinymce',
  'djangosecure'
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'professional.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(BASE_DIR, 'website/templates/'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'professional.context_processors.resume_context'
      ],
    },
  },
]

WSGI_APPLICATION = 'professional.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASE_URL=$(heroku config:get DATABASE_URL -a joshua-raanan-professional)

if not secret:
  DATABASES = {}
  DATABASES['default'] =  dj_database_url.config()
  DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# MEDIA Variables are used for user uploaded images
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, "professional", "static"),
  os.path.join(BASE_DIR, "website", "static"),
]

# Absolute path to the directory static files should be collected to
STATIC_ROOT = os.path.join(BASE_DIR, "static")

ADMIN_URL_PREFIX = '/admin/'

################################################################
####                         TinyMCE                         ###
################################################################
TINYMCE_COMPRESSOR = False
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'relative_urls': False,
    'convert_urls' : False,
    'width': '750px',
    'height': '350px',
    'forced_root_block': "",
    'plugins': 'advlist, lists, spellchecker',
    'theme_advanced_buttons1': 'bold,italic,underline,strikethrough,|,sub,sup,|,fontselect,fontsizeselect,formatselect,|,forecolor,backcolor,|,charmap',
    'theme_advanced_buttons2': 'bullist,numlist,|,justifyleft,justifycenter,justifyright,justifyfull,|,link,unlink,image,|,outdent,indent,|,undo,redo,|,visualaid,removeformat,cleanup,code,spellchecker,help',
}
# TINYMCE_SPELLCHECKER = True

if not secret:
  SECURE_SSL_REDIRECT = True