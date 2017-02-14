#!/usr/bin/python

from flask import Blueprint, redirect, request, render_template, session, url_for

# Teacher controller instance.
controller = Blueprint('teacher', __name__)

@controller.route('/dashboard')
def profile():
    """
    """
    return ''

@controller.route('/invite')
def invite():
    """
    """
    return ''