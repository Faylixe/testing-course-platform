#!/usr/bin/python

""" To document. """

from flask import Blueprint, render_template, request, redirect, session
from common import github_client
from common.access import get_current_user, restricted
from model.user import User

# Backend controller instance.
controller = Blueprint('student', __name__, template_folder='templates')

@restricted
@controller.route('/dashboard')
def dashboard():
    """ /student endpoint """
    # TODO : Retrieve metadata.
    return render_template('dashboard.html', current=get_current_user())