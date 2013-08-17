# -*- coding: utf-8 -*-
#
# Created on 7/28/13

"""Common settings and globals."""

from os import listdir, mkdir
from os.path import abspath, basename, dirname, join, normpath, isdir, exists
from sys import path, stderr


########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Your Name', 'your_email@example.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

ADMIN_URL = '/admin/'
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/Los_Angeles'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# Module name to format dates and hours with specific locales
FORMAT_MODULE_PATH = 'project.formats'

# Default formatting for time and date
DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y H:i'
TIME_FORMAT = 'H:i'
YEAR_MONTH_FORMAT = 'F Y'
MONTH_DAY_FORMAT = 'j. F'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

LOCALE_PATHS = tuple(join(join(SITE_ROOT, subdir), 'locale') for subdir in
                     listdir(SITE_ROOT) if isdir(join(SITE_ROOT, subdir)))
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


def define_assets_path(local_root_path):
    """Get or create system path to resources"""

    # Absolute filesystem path to the directory that will hold user-uploaded
    # files. Example: "/home/media/media.lawrence.com/media/"
    MEDIA_ROOT = join(local_root_path, 'media')
    try:
        if exists(local_root_path) and not exists(MEDIA_ROOT):
            mkdir(MEDIA_ROOT)
    except OSError:
        # Need this to log into stderr for tracking problems.
        # On Apache, this will be redirect to the ErrorLog.
        print >>stderr, 'Cannot create {0} folder'.format(MEDIA_ROOT)

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    STATIC_ROOT = join(local_root_path, 'assets')
    try:
        if exists(local_root_path) and not exists(STATIC_ROOT):
            mkdir(STATIC_ROOT)
    except OSError:
        print >>stderr, 'Cannot create {0} folder'.format(STATIC_ROOT)

    return MEDIA_ROOT, STATIC_ROOT
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = r"{{ secret_key }}"
########## END SECRET CONFIGURATION


########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
########## END SITE CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'sekizai.context_processors.sekizai',

    '{{ project_name }}.context_processors.debug_local',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)


# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    # 'johnny.middleware.LocalStoreClearMiddleware',
    # 'johnny.middleware.QueryCacheMiddleware',
]
########## END MIDDLEWARE CONFIGURATION

########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    # Database migration helpers:
    'south',

    'raven',
    'sekizai',
    'django_extensions',
    'compressor',
)

# Apps specific for this project go here.
LOCAL_APPS = (
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
def define_logger(log_level, logs_path_sys=None):
    """Create the dict of parameters for logging."""
    if not logs_path_sys or not exists(logs_path_sys):
        logs_path = join(SITE_ROOT, 'logs')
        if not exists(logs_path):
            try:
                mkdir(logs_path)
            except OSError:
                # Need this to log into stderr for tracking problems.
                # On Apache, this will be redirect to the ErrorLog.
                print >>stderr, 'Cannot create {0} folder'.format(logs_path)
    else:
        logs_path = logs_path_sys

    logging_dict = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'formatters': {
            'standard': {
                'format': '%(levelname)s %(asctime)s %(name)s.%(module)s.'
                          '%(funcName)s:L%(lineno)d ProcessNo:%(process)d/'
                          'ThreadNo:%(thread)d "%(message)s"',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
            'normative': {
                'format': '%(levelname)s %(asctime)s %(module)s.'
                          '%(funcName)s:L%(lineno)d "%(message)s"',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'django.utils.log.NullHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
            'errors': {
                'level': 'WARNING',
                'class': '{{ project_name }}.utils.print_helpers'
                         '.SplitStreamHandler',
                'formatter': 'normative'
            },
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.handlers.SentryHandler',
            },
            'default_file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': join(logs_path, '{{ project_name }}.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 5,
                'formatter': 'standard',
            },
            'tests_file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': join(logs_path, '{{ project_name }}-tests.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 5,
                'formatter': 'standard'
            },
            'mail_admins': {
                'level': 'ERROR',
                'include_html': True,
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['sentry'],
                'propagate': True,
                'level': 'INFO',
            },
            'django.request': {
                'handlers': ['sentry', 'mail_admins', 'errors'],
                'propagate': False,
                'level': log_level,
            },
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['sentry', 'console', 'errors'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['sentry', 'console'],
                'propagate': True,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['sentry', 'console'],
                'propagate': False,
            },
            'default': {
                'handlers': ['sentry', 'default_file', 'errors', 'console'],
                'propagate': True,
                'level': 'INFO',
            },
            'test': {
                'handlers': ['tests_file', 'errors', 'console'],
                'propagate': True,
                'level': 'DEBUG',
            },
        }
    }

    if log_level == 'DEBUG':
        # make all loggers use the console.
        for logger in logging_dict['loggers']:
            logging_dict['loggers'][logger]['handlers'] = ['console']

    return logging_dict
########## END LOGGING CONFIGURATION


########## CSS / JS / LESS COMPRESSOR (require dep: lessc)
COMPRESS_ENABLED = False
COMPRESS_OUTPUT_DIR = 'c'
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)
#COMPRESS_CACHE_BACKEND = 'compressor'

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
COMPRESS_PRECOMPILERS = (
    ('text/less', '/usr/local/bin/lessc {infile} {outfile}'),
)

COMPRESS_PARSER = 'compressor.parser.HtmlParser'
########## END COMPRESSION CONFIGURATION

########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '{{ project_name}}.wsgi.application'
########## END WSGI CONFIGURATION

########## TOOLBAR CONFIGURATION
ALLOWED_DEBUGGERS = []


def set_toolbar():
    """Set toolbar options"""
    def benchmark_callback(request):
        """Check if 'benchmark' is in GET parameters to deactivate
        debug_toolbar"""
        if request.user.username in ALLOWED_DEBUGGERS:
            return True
        else:
            return False
    extra_installed_apps = (
        'debug_toolbar',
    )
    MIDDLEWARE_CLASSES.append(
        'debug_toolbar.middleware.DebugToolbarMiddleware',)

    # IPs allowed to see django-debug-toolbar output.
    INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', '192.168.*.*',)

    DEBUG_TOOLBAR_CONFIG = {
        # If set to True (default), the debug toolbar will show an
        # intermediate page upon redirect so you can view any debug
        # information prior to redirecting. This page will provide a link
        # to the redirect destination you can follow when ready. If set to
        # False, redirects will proceed as normal.
        'INTERCEPT_REDIRECTS': False,

        # If not set or set to None, the debug_toolbar middleware will use
        # its built-in show_toolbar method for determining whether the
        # toolbar should show or not. The default checks are that DEBUG
        # must be set to True and the IP of the request must be in
        # INTERNAL_IPS. You can provide your own method for displaying the
        # toolbar which contains your custom logic.

        # method should return True or False.
        'SHOW_TOOLBAR_CALLBACK': benchmark_callback,

        # An array of custom signals that might be in your project, defined
        # as the python path to the signal.
        'EXTRA_SIGNALS': [],

        # If set to True (the default) then code in Django itself won't be
        # shown in SQL stacktraces.
        'HIDE_DJANGO_SQL': True,

        # If set to True (the default) then a template's context will be
        # included with it in the Template debug panel. Turning this off is
        # useful when you have large template contexts, or you have template
        # contexts with lazy data structures that you don't want to be
        # evaluated.
        'SHOW_TEMPLATE_CONTEXT': True,

        # If set, this will be the tag to which debug_toolbar will attach
        # the debug toolbar. Defaults to 'body'.
        'TAG': 'body',

        # If set, this will show stacktraces for SQL queries and cache calls.
        # Enabling stacktraces can increase the CPU time used when executing
        # queries. Defaults to True.
        'ENABLE_STACKTRACES': True,
    }

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.cache.CacheDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )

    return extra_installed_apps
########## END TOOLBAR CONFIGURATION