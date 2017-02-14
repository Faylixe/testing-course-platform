#!/usr/bin/python

from os import environ as env

from flask import Flask
from flask.ext.github import GitHub

application = Flask(__name__)
application.config['GITHUB_CLIENT_ID'] = env['GITHUB_CLIENT_ID']
application.config['GITHUB_CLIENT_SECRET'] = env['GITHUB_CLIENT_SECRET']

github = GitHub(application)

@application.route('/login')
def login():
    """ /login endpoint. """
    return github.authorize()

@application.route('/login/github')
@github.authorized_handler
def authorized(oauth_token):
    """
    :param oauth_token:
    """
    pass

if __name__ == '__main__':
    pass