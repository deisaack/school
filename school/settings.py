import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '2o4=&n-$_+a8f9+@o$l%0)pqk_9#0do3)wdjtvpi2ns*o+%&ng'

DEBUG = True

ALLOWED_HOSTS = []

from django.urls import reverse_lazy

INSTALLED_APPS = [
    'django.contrib.auth',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'school.authentication',
    'school.utils',

    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'braces',
    'easy_thumbnails',
    'authtools',
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

ROOT_URLCONF = 'school.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'school.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CRISPY_TEMPLATE_PACK = 'bootstrap3'

LOGIN_URL = reverse_lazy("auth:login")
LOGIN_REDIRECT_URL = reverse_lazy('home')

THUMBNAIL_EXTENSION = 'png'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'live/static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'live/media')

# CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_ALLOW_NONIMAGE_FILES = False
MATHJAX_ENABLED=True
MATHJAX_LOCAL_PATH = 'js/libs/mathjax/'
from school.utils.my_ck import CKEDITOR_CONFIGS
CKEDITOR_CONFIGS = CKEDITOR_CONFIGS