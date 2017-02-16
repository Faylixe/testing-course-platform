#!/usr/bin/python

""" To document. """

from functools import wraps
from flask import session, redirect, url_for
from blueprints.setup import is_setup
from model.user import User

def teacher_restricted():
    """Decorator function for page that required signed in users.

    :param previous: Page to redirect in case of failure.
    :returns: Decorated function.
    """
    def decorator(function):
        @wraps(function)
        def decorated(*args, **kwargs):
            if is_setup():
                user = get_current_user()
                if user is not None and user.type == User.TEACHER:
                    return function(*args, **kwargs)
            return redirect('/')
        return decorated
    return decorator

def student_restricted():
    """Decorator function for page that required signed in users.

    :param previous: Page to redirect in case of failure.
    :returns: Decorated function.
    """
    def decorator(function):
        @wraps(function)
        def decorated(*args, **kwargs):
            if is_setup():
                user = get_current_user()
                if user is not None and user.type == User.STUDENT:
                    return function(*args, **kwargs)
            return redirect('/')
        return decorated
    return decorator

def get_current_user():
    """Simple sugar method for retrieving current user instance if any.

    :returns: Current user if any, None otherwise.
    """
    if 'current_user' in session:
        return User.query.filter_by(github_id=session['current_user']).first()
