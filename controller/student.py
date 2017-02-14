#!/usr/bin/python

from flask import Blueprint, redirect, request, render_template, session, url_for

# Student controller instance.
controller = Blueprint('student', __name__)

@controller.route('/register')
def register():
    """
    """
    pass

@controller.route('/repository', methods=['POST'])
def set_repository():
    """
    """
    repository = request.form['repository']

@controller.route('/dashboard')
def profile():
    """
    """
    return ''