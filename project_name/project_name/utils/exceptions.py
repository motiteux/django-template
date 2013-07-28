#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created on {% now "d-m-Y" %}

__all__ = [
    '{{ project_name | title }}Error',
    '{{ project_name | title }}IOError',
    '{{ project_name | title }}AssertionError',
    '{{ project_name | title }}NotImplementedError',
    '{{ project_name | title }}UnknownError',
]

import traceback

from utils.print_helpers import list_formatter


class {{ project_name | title }}Error(Exception):

    """Base class for exceptions in {{ project_name | title }}."""

    def __init__(self, message='', module_name=''):
        """Initialize Base Error class."""
        super({{ project_name | title }}Error, self).__init__(message)
        self.module_name = module_name
        # debug message -> check which module raised the exception
        if self.module_name:
            self.module_debug_msg = 'Exception raised in %s' % self.module_name
        else:
            self.module_debug_msg = ''

    def __unicode__(self):
        return self.message + ' Exception raised in %s.\n' % self.module_name


class {{ project_name | title }}IOError({{ project_name | title }}Error, IOError):

    """Exception for a I/O error in {{ project_name | title }}"""

    def __init__(self, message, module_name=''):
        """Take argument from base class in Initializer."""
        super({{ project_name | title }}IOError, self).__init__(message, module_name)


class {{ project_name | title }}AssertionError({{ project_name | title }}Error, AssertionError):

    """Exception for a Assertion error in {{ project_name | title }}"""

    def __init__(self, message, module_name=''):
        """Take argument from base class in Initializer."""
        super({{ project_name | title }}AssertionError, self).__init__(message, module_name)


class {{ project_name | title }}NotImplementedError({{ project_name | title }}Error, NotImplementedError):

    """Exception for a not yet implemented feature error in {{ project_name | title }}"""

    def __init__(self, message, name_feature, module_name=''):
        """Take argument from base class in Initializer."""
        super({{ project_name | title }}NotImplementedError, self).__init__(message, module_name)
        self.name_feature = name_feature


class {{ project_name | title }}UnknownError(KMSError):

    """Exception that needs to be reported to development. This class is
    derived from Base class Exception to make sure we catch all Exceptions
    that cannot be handled here. """

    def __init__(self, message, module_name):
        """Take argument from base class in Initializer."""
        super({{ project_name | title }}UnknownError, self).__init__(message)
        self.module_name = module_name

    def __str__(self):
        """Allow represent access for args."""
        return self.message + ' Exception raised in %s.\n' % self.module_name

    @staticmethod
    def report_issue(cur_logger, mod_log):
        """This method reports the location and the initial raised exception
        with its type, traceback and location. It redirects user to reporting
        such issue."""
        traceback.print_exc(limit=10)
        cur_logger.critical('Error not managed.\n\tPlease, contact {0} '
                            'with this traceback.\n\tExiting'.format(
                                list_formatter(__authors__, 'Author list')
                            ))
