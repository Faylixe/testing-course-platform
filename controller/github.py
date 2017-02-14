#!/usr/bin/python

from flask import Blueprint, redirect, request, render_template, session, url_for
from main import application

# Signup controller instance.
controller = Blueprint('github', __name__)

@controller.route('/signin')
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
    pass