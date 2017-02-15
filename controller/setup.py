#!/usr/bin/python

from flask import Blueprint, render_template
from common.github import github_client
from model.state import PlatformState

# Signup controller instance.
controller = Blueprint('setup', __name__)

def is_setup():
    """Indicates if this application is setup or not.

    :returns: True if this application already has been setup, False otherwise.
    """
    return PlatformState.get('setup') == 'True'
    
@controller.route('/')
def index():
    """ Setup index page. """
    return render_template('setup.html')

def setup(token):
    """
    """
    pass