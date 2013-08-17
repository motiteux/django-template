# -*- coding: utf-8 -*-
#
# Created on 7/28/13

from os import environ

from local import *

ALLOWED_DEBUGGERS = ['username']
INSTALLED_APPS += set_toolbar()

# Database (MySQL by default, but you can change the Engine here)
IMPORT_DEBUG_TOOLBAR = True
USE_CACHES = False

SECRET_KEY = r"{{ secret_key }}"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        },
        'USER': '{{ project_name }}',
        'PASSWORD': environ['DB_PASSWD'],
        'HOST': '127.0.0.1',
        'PORT': '',
        'NAME': '{{ project_name }}',
    }
}

# Temporarily for django-debug-toolbar (to be bumped to > 0.9.4 asap)
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)