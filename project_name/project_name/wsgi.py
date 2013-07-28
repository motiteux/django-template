#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created on {% now "d-m-Y" %}

import os
from os.path import abspath, dirname
from sys import path


# django.wsgi launched as a local symlink onto project.wsgi
SITE_ROOT = dirname(dirname(abspath(__file__)))
path.append(SITE_ROOT)

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "jajaja.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()