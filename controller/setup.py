#!/usr/bin/python

from flask import Blueprint, render_template, redirect, url_for
from common.github import github_client
from model.state import PlatformState

# Signup controller instance.
controller = Blueprint('setup', __name__)

#
STATE_KEY = 'setup'

def is_setup():
    """Indicates if this application is setup or not.

    :returns: True if this application already has been setup, False otherwise.
    """
    return PlatformState.get('setup') == 'True'
    
@controller.route('/')
def index():
    """ Setup index page. """
    if is_setup():
        return redirect(url_for('main.index'))
    return render_template('setup.html')

@controller.route('/teacher')
def setup(token):
    """
    :param token: Github access token of the course owner.
    """
    if is_setup():
        return redirect(url_for('main.index'))
    user = User.create(User.TEACHER, token)
    user.name = github_client.get('user')['login']
    database.session.add(user)
    database.session.commit()
    PlatformState.put(STATE_KEY, 'True')
    return redirect(url_for('main.index'))