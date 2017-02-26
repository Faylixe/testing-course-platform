#!/usr/bin/python

""" To document. """

from os import environ as env
from flask import Flask, redirect, render_template, session, url_for
from flaskext.markdown import Markdown
from common import github_client
from common.access import get_current_user
from model import configure_database
from model.user import User
# Configure target application.
application = Flask(__name__, static_url_path='/static')
application.secret_key = env['APPLICATION_SECRET_KEY']
application.config['GITHUB_CLIENT_ID'] = env['GITHUB_CLIENT_ID']
application.config['GITHUB_CLIENT_SECRET'] = env['GITHUB_CLIENT_SECRET']
application.config['SQLALCHEMY_DATABASE_URI'] = env['DATABASE_URL']
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#application.config['CDN_DOMAIN'] = env['CDN_DOMAIN']
application.app_context().push()

# Configures application modules.
configure_database(application)
github_client.init_app(application)
Markdown(application)

@github_client.access_token_getter
def get_github_token():
    """Github token access layer.

    :returns: Access token of the current user if any, None otherwise.
    """
    if 'github_token' in session:
        return session['github_token']

# Registers controller of the application.
from blueprints.setup import is_setup, controller as setup_controller
from blueprints.teacher import controller as teacher_controller
from blueprints.student import controller as student_controller

application.register_blueprint(setup_controller, url_prefix='/setup')
application.register_blueprint(teacher_controller, url_prefix='/teacher')
application.register_blueprint(student_controller, url_prefix='/student')

@application.route('/')
def index():
    """ /index endpoint.
    
    If application is not setup, trigger setup controller. If not check
    if user if connected to display dashboard or redirect to signin
    screen instead.
    """
    if is_setup():
        user = get_current_user()
        if user is None:
            return render_template('signin.html', action='Se connecter')
        if user.type == User.TEACHER:
            return redirect(url_for('teacher.dashboard'))
        elif user.type == User.STUDENT:
            return redirect(url_for('student.dashboard'))
        else:
            return ''
    return redirect(url_for('setup.index'))

@application.route('/signin')
def signin():
    """ /signin endpoint

    Trigger github client authentification process.
    """
    return github_client.authorize()

@application.route('/authorize')
@github_client.authorized_handler
def authorize(token):
    """ /authorize endpoint.

    Callback method for github authentification. If application is in setup
    mode then the connected user is upgrade as the course owner (teacher role).
    Otherwise standard student user is created.

    :param token: GitHub OAuth access token.
    """
    if token is None:
        application.logger.error('GitHub OAuth access token not provided')
        return redirect(url_for('.index'))
    session['github_token'] = token
    if not is_setup():
        return redirect(url_for('setup.teacher'))
    id = github_client.get('user')['id']
    session['current_user'] = id
    user = User.get(id, token)
    return redirect(url_for('.index'))

@application.route('/signout')
def signout():
    """ /signout endpoint.

    Logout current user and redirect to index.
    """
    session['current_user'] = None
    return redirect(url_for('.index'))

if __name__ == '__main__':
    application.run(debug=True)