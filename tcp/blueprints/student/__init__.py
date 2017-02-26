#!/usr/bin/python

""" To document. """

from flask import Blueprint, render_template, request, redirect, session
from common import github_client
from common.access import get_current_user, student_restricted
from model.user import User

# Backend controller instance.
controller = Blueprint('student', __name__, template_folder='templates')

@controller.route('/dashboard')
@student_restricted
def dashboard():
    """ /student endpoint """
    # TODO : Retrieve metadata.
    return render_template('student/dashboard.html', current=get_current_user())