#!/usr/bin/python

from flask import Blueprint, redirect, request, render_template, session, url_for
from common.github import github_client
from model.state import PlatformState

# Signup controller instance.
controller = Blueprint('setup', __name__)

def is_setup():
    """Indicates if this application is setup or not.

    :returns: True if this application already has been setup, False otherwise.
    """
    return PlaformState.get('setup') == 'True'
    
@controller.route('/')
def index():
    """
    """
    token = ''# TODO : Create token.
    PlatformState.put('setup_token', token)
    # TODO : Log token.
    
    return ''


def setup():
    """
    """