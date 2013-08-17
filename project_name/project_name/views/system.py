# -*- coding: utf-8 -*-
#
# Created on {% now "d-m-Y" %}

"""
Views for system use (logins, errors,...)
"""

__all__ = [
    'page_not_found',
    'server_error',
    'permission_denied_view',
]

import logging

from django.http import HttpResponseNotFound, HttpResponseServerError, \
    HttpResponseForbidden
from django.template.loader import render_to_string
from django.template import RequestContext


logger = logging.getLogger('default.views.system')


def page_not_found(request):
    """View for Error 404

    :param request: HttpRequest
    :return: HttpResponse
    """
    return HttpResponseNotFound(render_to_string("404.html",
                                                 RequestContext(request)))


def server_error(request):
    """View for Error 500

    :param request: HttpRequest
    :return: HttpResponse
    """
    return HttpResponseServerError(
        render_to_string("500.html",
                         RequestContext(request)))


def permission_denied_view(request, message=''):
    """View for Error 403

    :param request: HttpRequest
    :return: HttpResponse
    """
    return HttpResponseForbidden(
        render_to_string('403.html',
                         {'err_msg': message},
                         RequestContext(request)))
