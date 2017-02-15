#!/usr/bin/python

""" To document. """

from flask import Blueprint, render_template, redirect, url_for
from common.github import github_client
from model.state import PlatformState, StateCache

# Signup controller instance.
controller = Blueprint('setup', __name__)

# Configures associated plaform state value.
state_key = 'setup'
state_cache = StateCache(state_key)

def is_setup():
    """Indicates if this application is setup or not.

    :returns: True if this application already has been setup, False otherwise.
    """
    return state_cache.get() == 'True'
    
@controller.route('/')
def index():
    """ /setup endpoint """
    if is_setup():
        return redirect(url_for('tcp.index'))
    return render_template('signin.html', action='Setup')

@controller.route('/teacher')
def setup(token):
    """ /setup/teacher endpoint.
    
    Configures this application using given token for creating 
    course teacher user.

    :param token: Github access token of the course owner.
    """
    if is_setup():
        return redirect(url_for('tcp.index'))
    user = User.create(User.TEACHER, token)
    user.name = github_client.get('user')['login']
    database.session.add(user)
    database.session.commit()
    state_cache.set_value('1')
    return redirect(url_for('tcp.index'))