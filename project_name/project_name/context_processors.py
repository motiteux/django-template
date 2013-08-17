# -*- coding: utf-8 -*-

# Created on {% now "d-m-Y" %}

"""
Context processors for the whole project
"""

__all__ = [
    'debug_local',
]

from django.conf import settings


def debug_local(request):
    """Custom debug context proc"""
    return {'DEBUG_LOCAL': getattr(settings, 'DEBUG', False)}
