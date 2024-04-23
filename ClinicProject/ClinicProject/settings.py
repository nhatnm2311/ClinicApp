"""
Django settings for ClinicProject project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import pymysql
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_ROOT = '%s/ClinicApp/static' % BASE_DIR
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z48d)8k5xw!g&fd49d*pt4*c3m5ew*g+_$lq6!1lq!=&gc^efv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ClinicApp.apps.ClinicappConfig',
    'nested_inline',
    'admin_reorder',
    'rest_framework',
    'oauth2_provider',
    'social_django',
    'drf_social_oauth2',
    'drf_yasg',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ClinicApp.admin.Reorder',
]

ROOT_URLCONF = 'ClinicProject.urls'
AUTH_USER_MODEL = "ClinicApp.User"
CKEDITOR_UPLOAD_PATH = "images/CKEDITOR/"
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'ClinicProject.wsgi.application'

pymysql.install_as_MySQLdb()
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clinicdb',
        'USER': 'root',
        'PASSWORD': 'Admin@123',
        'HOST': ''
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/
DATETIME_FORMAT = '%d-%m-%Y %H:%M'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
L10N = False
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#OTHER SETTING


import cloudinary

cloudinary.config(
    cloud_name="dbbqoxmuf",
    api_key="746766982517857",
    api_secret="eWXAdIufgpm_IIU8D5GbJ4NdWVA"
)

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,
    'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.JSONParser',],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'drf_social_oauth2.authentication.SocialAuthentication',
    )
}
ADMIN_REORDER = (
    'sites',
    {
        'app': 'ClinicApp',
        'label': 'Overview',
        'models': (
            'ClinicApp.Department',
        )
    },
    {
        'app': 'ClinicApp',
        'label': 'Human Resource',
        'models': (
            'ClinicApp.User',
            'ClinicApp.Employee',
            'ClinicApp.Doctor',
            'ClinicApp.Nurse',
        )
    },
    {
        'app': 'ClinicApp',
        'label': 'Medicines',
        'models': (
            'ClinicApp.Medicine',
            'ClinicApp.Vendor',
            'ClinicApp.MedicinePrice',
        )
    },
    {
        'app': 'ClinicApp',
        'label': 'Schedule',
        'models': (
            'ClinicApp.Schedule',
        )
    },
)

oauth2_secret="rqWWMDFzefEOrYSAdh3eL1WgmzZVSAr6OnQrsrPt8FhSCg5OOa1p3Nr4ezVehesaeKX2FAr0jwPwQ4sdl36mYCftSga3OCGyL1AkS0RIMxkjB1YehoAgQLlJZEauBnzH"
OAUTH2_PROVIDER = {'OAUTH2_BACKEND_CLASS': 'oauth2_provider.oauth2_backends.JSONOAuthLibCore'}
#GMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'minhnhat.nmn02@gmail.com'
EMAIL_HOST_PASSWORD = "rei0333953974"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'

#social
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'drf_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "612635500018-r9bm3h8bmmqqoup3nsfuqfd1cf0fcpv4.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"

# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    ]