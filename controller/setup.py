#!/usr/bin/python

from flask import Blueprint, redirect, request, render_template, session, url_for
from main import github

# Signup controller instance.
controller = Blueprint('setup', __name__)

def is_setup():
    """Indicates if this application is setup or not.

    :returns: True if this application already has been setup, False otherwise.
    """
    return False
    
@controller.route('/')
def index():
    """
    """
    # TODO : Create token.
    # TODO : Write token to config (DB or DS ?)
    return ''

@controller.route('/signup')
def signup():
    """
    """
    token = None # Retrieve.
    # TODO : Check if token is valid.
    return github.authorize()

@application.route('/b')
@github.authorized_handler
def authorized(oauth_token):
    """
    :param oauth_token:
    """
    return ''


def setup():
    """
    """