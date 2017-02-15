#!/usr/bin/python

from os import environ as env
from flask import Flask
from model import database
#from flask_cdn import CDN
from common.github import github_client
from controller.setup import is_setup, controller as setup_controller
from controller.teacher import controller as teacher_controller
from controller.student import controller as student_controller

# Application creation / configuration.
application = Flask(__name__, static_url_path='/static')
application.secret_key = env['APPLICATION_SECRET_KEY']
application.config['GITHUB_CLIENT_ID'] = env['GITHUB_CLIENT_ID']
application.config['GITHUB_CLIENT_SECRET'] = env['GITHUB_CLIENT_SECRET']
application.config['SQLALCHEMY_DATABASE_URI'] = env['DATABASE_URL']
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
application.config['SQLALCHEMY_ECHO'] = True
#application.config['CDN_DOMAIN'] = env['CDN_DOMAIN']

@application.route('/signin')
def signup():
    """ Github signup entry point. """
    return github_client.authorize()

@application.route('/token')
@github_client.authorized_handler
def authorized(oauth_token):
    """
    :param oauth_token:
    """
    next_url = request.args.get('next') or url_for('index') # TODO : check for setup.
    if oauth_token is None:
        flash("Authorization failed.") # TODO : Manage error.
        return redirect(next_url)
    if is_setup():
        pass # TODO : Redirect.
    user = User.query.filter_by(token=oauth_token).first()
    if user is None:
        user = User()
        user.token = oauth_token
        database.add(user)
    user.oauth_token = oauth_token
    database.commit()
    return redirect(next_url)

@github_client.access_token_getter
def token_getter():
    user = g.user # TODO : Get from session.
    if user is not None:
        return user.oauth_token
        
if __name__ == '__main__':

    application.app_context().push()
    #cdn = CDN()
    github_client.init_app(application)
    from model.state import PlatformState
    from model.user import User
    database.init_app(application)
    database.create_all()
    database.session.commit()
    application.register_blueprint(setup_controller, url_prefix='/setup')
    if is_setup():
        application.register_blueprint(student_controller, url_prefix='/student')
        application.register_blueprint(teacher_controller, url_prefix='/teacher')
     # TODO : Check if CDN mode
    # cdn.init_app(application)
    application.run(debug=True)