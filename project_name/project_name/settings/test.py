# -*- coding: utf-8 -*-
#
# Created on 7/28/13

"""
This set of settings is for drastically speed up unit test by using sqlite3,
instead
of MySQL (the whole DB is then created in memory) and skip the migration with
 South.

Based on:
    http://www.dominicrodger.com/faster-django-tests.html
    https://docs.djangoproject.com/en/1.4/topics/testing/#speeding-up-the-tests

"""

import tempfile
from os import mkdir
from os.path import join

from base import *


TMP_ROOT = tempfile.mkdtemp(prefix='{{ project_name }}_dev')
mkdir(join(TMP_ROOT, 'local_root'))

LOCAL_ROOT = join(TMP_ROOT, 'local_root')
mkdir(join(TMP_ROOT, 'db'))

LOGGING = define_logger('INFO')
MEDIA_ROOT, STATIC_ROOT = define_assets_path(LOCAL_ROOT)

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
########## END MIDDLEWARE CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(TMP_ROOT, 'db', 'test_sqlite.db'),
    }
}
########## END DATABASE CONFIGURATION


SOUTH_TESTS_MIGRATE = False  # To disable migrations and use syncdb instead
SKIP_SOUTH_TESTS = True  # To disable South's own unit tests