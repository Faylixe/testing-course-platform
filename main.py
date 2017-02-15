#!/usr/bin/python

from os import environ as env
from flask import Flask, redirect, session, url_for
from model import database
#from flask_cdn import CDN
from common.github import github_client
from controller.setup import is_setup, controller as setup_controller
from controller.teacher import controller as teacher_controller
from controller.student import controller as student_controller

application = Flask(__name__, static_url_path='/static')
application.secret_key = env['APPLICATION_SECRET_KEY']
application.config['GITHUB_CLIENT_ID'] = env['GITHUB_CLIENT_ID']
application.config['GITHUB_CLIENT_SECRET'] = env['GITHUB_CLIENT_SECRET']
application.config['SQLALCHEMY_DATABASE_URI'] = env['DATABASE_URL']
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
application.config['SQLALCHEMY_ECHO'] = True
#application.config['CDN_DOMAIN'] = env['CDN_DOMAIN']

application.app_context().push()
from model.state import PlatformState
from model.user import User
database.init_app(application)
database.create_all()
database.session.commit()

github_client.init_app(application)

application.register_blueprint(setup_controller, url_prefix='/setup')
application.register_blueprint(student_controller, url_prefix='/student')
application.register_blueprint(teacher_controller, url_prefix='/teacher')

@application.route('/')
def index():
    """ """
    if is_setup():
        return ''
    return redirect('/setup/')

def get_current_user():
    """
    """
    if 'current_user' in session:
        return User.query().filter_by(id=session['current_user']).first()

@application.route('/signin')
def signup():
    """ Github signup entry point. """
    return github_client.authorize()

@application.route('/token')
@github_client.authorized_handler
def authorized(token):
    """
    :param token:
    """
    if token is None:
        # TODO : Display error ?
        return redirect('.index')
    if is_setup():
        return redirect(url_for('setup.teacher', token=token))
    user = User.get(token)
    user.token = token
    database.session.commit()
    session['current_user'] = user.id
    return redirect('.index')

@github_client.access_token_getter
def token_getter():
    """ Github token access layer. """
    user = get_current_user()
    if user is not None:
        return user.token
        
if __name__ == '__main__':
    #cdn = CDN()
     # TODO : Check if CDN mode
    # cdn.init_app(application)
    application.run(debug=True)