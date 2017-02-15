#!/usr/bin/python

from functools import wraps
from flask import session, redirect, url_for
from controller.setup import is_setup

def require_application_setup():
    """ Decorator function for page that required signed in users. """
    def decorator(function):
        @wraps(function)
        def decorated(*args, **kwargs):
            if is_setup:
                return function(*args, **kwargs)
            return redirect(url_for('tcp.index'))
        return decorated
    return decorator

def restricted(previous='tcp.index'):
    """Decorator function for page that required signed in users.
    :param previous:
    """
    def decorator(function):
        @wraps(function)
        def decorated(*args, **kwargs):
            if 'current_user' in session:
                return function(*args, **kwargs)
            return redirect(previous)
        return decorated
    return decorator