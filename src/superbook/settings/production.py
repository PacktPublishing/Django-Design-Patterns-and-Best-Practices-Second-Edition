# In production set the environment variable like this:
#    DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production
from .base import *             # NOQA

import dj_database_url
from decouple import config, Csv

# For security and performance reasons, DEBUG is turned off
SECRET_KEY = config('SECRET_KEY', default="not-a-secret")
DEBUG = config('DEBUG', default=False, cast=bool)
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}
DATABASES['default']['CONN_MAX_AGE'] = 500
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

TEMPLATE_DEBUG = DEBUG

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

WSGI_APPLICATION = 'src.superbook.wsgi.application'

# in your settings file
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}
