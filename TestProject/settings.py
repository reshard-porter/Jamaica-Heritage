"""
Django settings for TestProject project.

Updated to run on current Django (5.2 LTS) and Python 3.10+.
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
# Set DJANGO_SECRET_KEY in the environment for anything beyond local development.
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-*9s!t!@lgoc#l^+%v=%rj3*e-it0k0r%g(h0jqtad-q==t(bb9',
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', '1') == '1'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'Posts.apps.PostsConfig',
    'Heritage.apps.HeritageConfig',
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
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TestProject.urls'

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
                'Heritage.context_processors.heritage_nav',
            ],
        },
    },
]

WSGI_APPLICATION = 'TestProject.wsgi.application'


# Database
# Default: SQLite (no setup needed). To use MySQL instead, set DB_ENGINE=mysql
# and optionally DB_NAME / DB_USER / DB_PASSWORD / DB_HOST / DB_PORT.

if os.environ.get('DB_ENGINE', 'sqlite').lower() == 'mysql':
    # Use PyMySQL as a drop-in for mysqlclient if mysqlclient isn't installed.
    # This must run here, before Django loads the MySQL backend.
    try:
        import MySQLdb  # noqa: F401
    except ImportError:
        import pymysql
        # Django 5.2 checks for mysqlclient >= 2.2.1; PyMySQL reports an older
        # version number by default, so report a compatible one.
        pymysql.version_info = (2, 2, 7, 'final', 0)
        pymysql.install_as_MySQLdb()

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME', 'django'),
            'USER': os.environ.get('DB_USER', 'root'),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
            'PORT': os.environ.get('DB_PORT', '3306'),
            'OPTIONS': {'charset': 'utf8mb4'},
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Referrer policy
# Django defaults to 'same-origin', which strips the Referer header from
# cross-site requests. YouTube's embedded player needs it, and fails with
# "Error 153: Video player configuration error" without it. This value sends
# only the site's origin (e.g. http://127.0.0.1:8000) to other sites.
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
