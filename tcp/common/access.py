#!/usr/bin/python

""" To document. """

from functools import wraps
from flask import session, redirect, url_for
from blueprints.setup import is_setup
from model.user import User

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

def get_current_user():
    """Simple sugar method for retrieving current user instance if any.

    :returns: Current user if any, None otherwise.
    """
    if 'current_user' in session:
        return User.query.filter_by(github_id=session['current_user']).first()
