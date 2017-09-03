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

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8cggf_jv#0@d=ltzef@rmv%ne_lo^_xnz2+)#jzh5xh_e(l64o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['joshua-raanan-professional.herokuapp.com','joshua-raanan.com']


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
  'tinymce'
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
      ],
    },
  },
]

WSGI_APPLICATION = 'professional.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'professional',
    #DEFINED USING heroku config:set for prod, import settings_secret.py for dev
    'USER': os.environ.get('DATABASE_DEFAULT_USER'),
    'PASSWORD': os.environ.get('DATABASE_DEFAULT_PASSWORD'),
    'HOST': os.environ.get('DATABASE_DEFAULT_HOST'),
    'PORT':os.environ.get('DATABASE_DEFAULT_PORT'),
  }
}


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