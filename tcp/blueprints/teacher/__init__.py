#!/usr/bin/python

""" To document. """

from flask import Blueprint, render_template, request, redirect, session
from common.github import github_client
from common.access import restricted
from model.user import User

# Backend controller instance.
controller = Blueprint('teacher', __name__, template_folder='templates')

@controller.route('/')
@restricted
def index():
    """ /teacher endpoint """
    # TODO : Retrieve metadata.
    return render_template('dashboard.html')