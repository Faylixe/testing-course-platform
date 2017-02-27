#!/usr/bin/python

""" To document. """

from flask import Blueprint, render_template, request, redirect, session
from common import github_client
from common.access import get_current_user, student_restricted
from model.user import User
from model.state import REPOSITORY_KEY

# Backend controller instance.
controller = Blueprint('student', __name__, template_folder='templates')

def has_fork_ready():
    """Indicates if the current user has a fork of the target project.

    :returns: True if the fork is ready, False otherwise.
    """
    target = PlatformState.get(REPOSITORY_KEY)
    repositories = github_client.get('/user/repos', params={ 'visibility': 'public', 'affiliation': 'owner' })
    for repository in repositories:
        if repository.name == target and repository.fork:
            # TODO : Check if repository is a valid fork of the target one.
            return True
    return False

def on_fork_ready(user):
    """
    """
    # TODO : Set user repository.
    # TODO : Adds teacher as collaborator.
    # TODO : Creates first exercice.
    pass

@controller.route('/dashboard')
@student_restricted
def dashboard():
    """ /student endpoint """

    user = get_current_user()
    if has_fork_ready():
        if user.repository is None:
            on_fork_ready(user)
        # TODO : Retrieve metadata.
        return render_template('student/dashboard.html', current=user)
    return render_template('student/waiting_fork.html')