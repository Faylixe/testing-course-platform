#!/usr/bin/python

""" To document. """

from os import environ as env
from flask import Flask, redirect, session, url_for
from model import configure_database
from model.user import User
from common.github import github_client

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

# Registers controller of the application.
from controller.setup import is_setup, controller as setup_controller
application.register_blueprint(setup_controller, url_prefix='/setup')

@application.route('/')
@application.route('/index')
def index():
    """ /index endpoint.
    
    If application is not setup, trigger setup controller. If not check
    if user if connected to display dashboard or redirect to signin
    screen instead.
    """
    if is_setup():
        user = get_current_user()
        if user is None:
            return render_template('signin.html', action='Signin')
        return render_template('dashboard.html', user=user)
    return redirect('/setup/')

def get_current_user():
    """Simple sugar method for retrieving current user instance if any.

    :returns: Current user if any, None otherwise.
    """
    if 'current_user' in session:
        return User.query().filter_by(id=session['current_user']).first()

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
    if is_setup():
        return redirect(url_for('setup.teacher', token=token))
    user = User.get(token)
    user.token = token
    database.session.commit()
    session['current_user'] = user.id
    return redirect('.index')

@github_client.access_token_getter
def token_getter():
    """Github token access layer.

    :returns: Access token of the current user if any, None otherwise.
    """
    user = get_current_user()
    if user is not None:
        return user.token

if __name__ == '__main__':
    application.run(debug=True)