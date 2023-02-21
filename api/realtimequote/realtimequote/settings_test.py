from realtimequote.settings import *

DEBUG = True

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# Celery
CELERY_TASK_ALWAYS_EAGER = True
CELERY_BROKER_URL = config("CELERY_BROKER_URL", "memory://")
