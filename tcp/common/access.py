#!/usr/bin/python

""" To document. """

from functools import wraps
from flask import session, redirect, url_for
from controller.setup import is_setup

def restricted(previous='tcp.index'):
    """Decorator function for page that required signed in users.

    :param previous: Page to redirect in case of failure.
    :returns: Decorated function.
    """
    def decorator(function):
        @wraps(function)
        def decorated(*args, **kwargs):
            if is_setup and 'current_user' in session:
                return function(*args, **kwargs)
            return redirect(previous)
        return decorated
    return decorator