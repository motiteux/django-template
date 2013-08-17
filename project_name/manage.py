#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created on {% now "d-m-Y" %}

"""
Entry-point for {{ project_name }}
"""

import os
import sys

MANAGE_FILEPATH = os.path.realpath(sys.argv[0])

DJANGO_CMD_ROOT = os.path.dirname(MANAGE_FILEPATH)
sys.path.append(DJANGO_CMD_ROOT)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.dev_marco")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
