# -*- coding: utf-8 -*-
#
# Created on {% now "d-m-Y" %}

import os

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView, RedirectView
from django.contrib import admin


admin.autodiscover()


#TODO: 500 page should be done static (using statictemplate for example)
handler403 = '{{ project_name}}.views.system.permission_denied_view'
handler404 = '{{ project_name}}.views.system.page_not_found'
handler500 = '{{ project_name}}.views.system.server_error'
handler504 = '{{ project_name}}.views.system.server_error'

# i18n
js_info_dict = {
    # 'domain': 'djangojs',
    'packages': ('project', ),
}


def i18n_javascript(request):
    """Use translation in javascript from request

    :param request:
    :return:
    """
    return admin.site.i18n_javascript(request)

urlpatterns = patterns(
    '',
    # url(r'^jsi18n/(?P<packages>\S+?)/$',
    #     'django.views.i18n.javascript_catalog'),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict, name="custom-jsi18n"),
)

urlpatterns += staticfiles_urlpatterns()


urlpatterns += patterns(
    '',
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^admin/jsi18n', i18n_javascript),
    url(r'^IEStandards\.xml/$', RedirectView.as_view(
        url=os.path.join(settings.STATIC_URL, 'IEStandards.xml'))),
)

urlpatterns = i18n_patterns(
    '',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    url(r'^$', TemplateView.as_view(template_name='base.html')),
)


# Used only to get rid of some media-related errors on development servers.
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^favicon\.ico/$', RedirectView.as_view(
            url=os.path.join(settings.STATIC_URL, 'img/ico/favicon.png'))
            ),

        # Serving media files only in Dev mode by Django
        url(r'^' + settings.MEDIA_URL.lstrip('/') + '(?P<path>.*)$',
            'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True},),
    )

    urlpatterns += i18n_patterns(
        '',
        # Enabled in Dev mode to test error pages
        (r'^404/', handler404),
        (r'^403/', handler403),
        (r'^500/', handler500),
        (r'^504/', handler504),
    )
