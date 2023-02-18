"""
Django settings for realtimequote project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from decouple import config
from urllib.parse import urlparse
from kombu import Exchange, Queue



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DB_URI = config(
    "DB_URI", default="postgresql://postgres:postgres@localhost/tradex", cast=str
)
AUTHENTICATOR_URI = config(
    "AUTHENTICATOR_URI", default="http://localhost:8001", cast=str
)
uri_params = urlparse(DB_URI)
DB_HOST = uri_params.hostname
DB_USER = uri_params.username
DB_PASS = uri_params.password
DB_NAME = uri_params.path.strip("/")
BROKER_URL = config("BROKER_URL", default="amqp://root:secret@localhost:5672//", cast=str)
ENVIRONMENT = config("SIMPLE_SETTINGS", "realtimequote.realtimequote.settings").split(".")[-1:][0]


# Django timezones and languages settings
# https://docs.djangoproject.com/en/4.1/ref/settings
TIME_ZONE = "UTC"
USE_TZ = True
USE_I18N = False
LANGUAGE_CODE = "en"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u)^c2w8nhc*ulj4ih1t0)4(np^_s(0mo*ly23b1pzqei4396^k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

DATA_UPLOAD_MAX_MEMORY_SIZE = 10*1024*1024  # 10MB
CORS_ORIGIN_ALLOW_ALL = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 60 * 60


# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    "django_filters",
    "celery",
    "django_celery_beat",
    "django_celery_results"
]


LOCAL_APPS = [
    'coin.apps.CoinConfig',
    'quotation.apps.QuotationConfig'
]


INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "middlewares.authentication.JWTAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_PAGINATION_CLASS': 'middlewares.pagination.CustomPagination',
    'PAGE_SIZE': 10,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = 'realtimequote.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'realtimequote.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "OPTIONS": {"options": "-c search_path=public"},
        "HOST": DB_HOST,
        "USER": DB_USER,
        "PASSWORD": DB_PASS,
        "NAME": DB_NAME,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Celery Configuration Global
# https://docs.celeryproject.org/en/latest/userguide/configuration.html
CELERY_BROKER_URL = BROKER_URL
CELERY_WORKERS = config("CELERY_WORKERS", default=1, cast=int)
CELERY_TIME_ZONE = TIME_ZONE
CELERY_ENABLE_UTC = True
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_CONTENT_ENCODING = "utf-8"
CELERY_ALWAYS_EAGER = False
CELERY_WORKER_MAX_TASKS_PER_CHILD = 3

# Celery Configuration "Django Celery Beat"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# Celery Configuration "Celery Result Backend"
CELERY_RESULT_BACKEND = "django-db"
DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH = 191

# Celery Configuration "Flower"
CELERY_WORKER_ENABLE_REMOTE_CONTROL = False
CELERY_WORKER_SEND_TASK_EVENTS = False
CELERY_FLOWER_BASIC_AUTH = config("CELERY_FLOWER_BASIC_AUTH", default="root:secret", cast=str)

# Celery Task Queues
CELERY_TASK_QUEUES = (
    Queue(
        name="task-collect-coin-quotation",
        exchange=Exchange("task-collect-coin-quotation", type="direct"),
        routing_key="task-collect-coin-quotation",
    ),
)


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/app/static/"
STATIC_ROOT = "./static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
