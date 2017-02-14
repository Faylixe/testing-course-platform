#!/usr/bin/python

from functools import wraps
from flask import session, redirect

def require_application_initialized():
    """ Decorator function for page that required signed in users. """
    def decorator(function):
        @wraps(function)
        def decorated(*args, **kwargs):
            if 'userId' in session:
                return function(*args, **kwargs)
            return redirect(previous)
        return decorated
    return decorator

def restricted(previous='/'):
    """Decorator function for page that required signed in users.
    :param previous:
    """
    def decorator(function):
        @wraps(function)
        def decorated(*args, **kwargs):
            if 'userId' in session:
                return function(*args, **kwargs)
            return redirect(previous)
        return decorated
    return decorator