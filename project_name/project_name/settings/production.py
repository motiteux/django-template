# -*- coding: utf-8 -*-
#
# Created on {% now "d-m-Y" %}

"""Production settings specifics. """

from os import environ

from base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = []
########## END HOST CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION

########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': '',
        'OPTIONS': {
        },
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'NAME': '',
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': dict(
        BACKEND='django.core.cache.backends.memcached.MemcachedCache',
        LOCATION=[''],
    ),
    'johnny': dict(
        BACKEND='johnny.backends.memcached.MemcachedCache',
        LOCATION=[''],
        JOHNNY_CACHE=True,
    ),
}
CACHE_MIDDLEWARE_SECONDS = 60

########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION


########## STATIC FILES CONFIGURATION
LOCAL_ROOT = get_env_setting('LOCAL_ROOT')
MEDIA_ROOT, STATIC_ROOT = define_assets_path(LOCAL_ROOT)
########## END STATIC FILES CONFIGURATION


########## LOGGING CONFIGURATION
LOGS_ROOT = get_env_setting('LOGS_ROOT')
LOGGING = define_logger(LOGS_ROOT, 'INFO')
########## END LOGGING CONFIGURATION


########## COMPRESSOR / JS / CSS / LESSC CONFIGURATION
LESSC_PATH = get_env_setting('LESSC_PATH')
COMPRESS_PRECOMPILERS = (
    ('text/less', LESSC_PATH + ' {infile} {outfile}'),
)

COMPRESS_ENABLED = True
########## END COMPRESSOR / JS / CSS / LESSC CONFIGURATION


########## DEBUGGING AND EXTRA LOGGING CONFIGURATION
ALLOWED_DEBUGGERS = ['username']
INSTALLED_APPS += set_toolbar()

try:
    import raven
except ImportError:
    pass
else:
    INSTALLED_APPS += (
        # Sentry client
        'raven.contrib.django.raven_compat',
    )
    RAVEN_CONFIG = {
        'dsn': '',
    }
########## END DEBUGGING AND EXTRA LOGGING CONFIGURATION
