#!/usr/bin/python

""" To document. """

from flask import Blueprint, render_template, request, redirect, session, url_for
from common import github_client
from model import database
from model.exercice import Exercice
from model.state import PlatformState, StateCache
from model.user import User

# Setup controller instance.
controller = Blueprint('setup', __name__, template_folder='templates')

# Configures associated plaform state value.

TEACHER_KEY = 'setup_teacher'
REPOSITORY_KEY = 'setup_repository'
teacher_cache = StateCache(TEACHER_KEY)
repository_cache = StateCache(REPOSITORY_KEY)

def is_repository_setup():
    """Indicates if base repository is setup or not.
    """
    return repository_cache.get_value() is not None

def is_teacher_setup():
    """Indicates if application teacher role is setup or not.
    """
    return teacher_cache.get_value() is not None

def is_setup():
    """Indicates if this application is setup or not.

    :returns: True if this application already has been setup, False otherwise.
    """
    return is_teacher_setup() and is_repository_setup()

@controller.route('/')
def index():
    """ /setup endpoint """
    if is_setup():
        return redirect('/')
    return render_template('signin.html', action='Demarrer')

@controller.route('/teacher')
def teacher():
    """ /setup/teacher endpoint.
    
    Configures this application using given token for creating 
    course teacher user.

    :param token: Github access token of the course owner.
    """
    if is_setup():
        return redirect('/')
    if is_teacher_setup():
        return redirect(url_for('setup.repository'))
    id = github_client.get('user')['id']
    user = User.create(User.TEACHER, id, session['github_token'])
    session['current_user'] = id
    teacher_cache.set_value('1')
    return redirect(url_for('setup.repository'))

# Filters for repository selection.
REPOSITORY_FILTERS = { 'visibility': 'public', 'affiliation': 'owner' }

@controller.route('/repository')
@controller.route('/repository/<repository_name>')
def repository(repository_name=None):
    """ /setup/repository endpoint.

    Allows teacher user to select original repository student will fork from.
    """
    if is_setup() or not is_teacher_setup():
        return redirect('/')
    teacher = User.query.filter_by(github_id=session['current_user']).first()
    repositories = github_client.get('user/repos', params=REPOSITORY_FILTERS)
    if repository_name is not None:
        # TODO : Ensure repository exists (security purpose).
        repository_cache.set_value(repository_name)
        return redirect('/')
    return render_template('setup/list_repositories.html', current=teacher, repositories=repositories)