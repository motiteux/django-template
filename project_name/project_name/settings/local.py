# -*- coding: utf-8 -*-
#
# Created on 7/28/13

"""Development settings and globals."""


from base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
IMPORT_DEBUG_TOOLBAR = False
USE_CACHES = False
CACHE_MIDDLEWARE_SECONDS = 0


LOGGING = define_logger('INFO')

MEDIA_ROOT, STATIC_ROOT = define_assets_path(SITE_ROOT)
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
if USE_CACHES:
    pass
else:
    ########## MIDDLEWARE CONFIGURATION
    try:
        MIDDLEWARE_CLASSES.remove(
            'django.middleware.cache.UpdateCacheMiddleware')
        MIDDLEWARE_CLASSES.remove(
            'django.middleware.cache.FetchFromCacheMiddleware',)
        MIDDLEWARE_CLASSES.remove(
            'johnny.middleware.LocalStoreClearMiddleware')
        MIDDLEWARE_CLASSES.remove(
            'johnny.middleware.QueryCacheMiddleware')
    except ValueError:
        pass

    CACHE_MIDDLEWARE_SECONDS = 0

    CACHES = {
        'default': dict(
            BACKEND='django.core.cache.backends.dummy.DummyCache',
        ),
    }
########## END CACHE CONFIGURATION


########## EXTRA 3rd APPS CONFIGURATION
try:
    import django_nose
except ImportError:
    pass
else:
    INSTALLED_APPS += (
        'django_nose',
    )
########## END EXTRA 3rd APPS CONFIGURATION
