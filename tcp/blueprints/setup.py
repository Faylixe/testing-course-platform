#!/usr/bin/python

""" To document. """

from flask import Blueprint, render_template, request, redirect, session
from common.github import github_client
from model import database
from model.state import PlatformState, StateCache
from model.user import User

# Setup controller instance.
controller = Blueprint('setup', __name__)

# Configures associated plaform state value.
state_key = 'setup'
state_cache = StateCache(state_key)

def is_setup():
    """Indicates if this application is setup or not.

    :returns: True if this application already has been setup, False otherwise.
    """
    return state_cache.get_value() == '1'
    
@controller.route('/')
def index():
    """ /setup endpoint """
    if is_setup():
        return redirect('/')
    return render_template('signin.html', action='Setup')

@controller.route('/teacher')
def teacher():
    """ /setup/teacher endpoint.
    
    Configures this application using given token for creating 
    course teacher user.

    :param token: Github access token of the course owner.
    """
    if is_setup():
        return redirect('/')
    token = request.args['token']
    user = User.create(User.TEACHER, token)
    session['current_user'] = user.id
    user.name = github_client.get('user')['login']
    database.session.add(user)
    database.session.commit()
    state_cache.set_value('1')
    return redirect('/')