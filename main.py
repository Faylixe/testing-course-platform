#!/usr/bin/python

from os import environ as env
from flask import Flask
from common.github import github_client
from controller.setup import is_setup, controller as setup_controller
from controller.teacher import controller as teacher_controller
from controller.student import controller as student_controller

# Application creation / configuration.
application = Flask(__name__)
application.secret_key = env['APPLICATION_SECRET_KEY']
application.config['GITHUB_CLIENT_ID'] = env['GITHUB_CLIENT_ID']
application.config['GITHUB_CLIENT_SECRET'] = env['GITHUB_CLIENT_SECRET']
application.config['SQLALCHEMY_DATABASE_URI'] = env['DATABASE_URL']

# Configure github client.
github_client.init_app(application)

# Database intialization.
database.init_app(application)
database.createTables()

# Registers application controllers.
application.register_blueprint(setup_controller, url_prefix='/setup')
if is_setup():
    application.register_blueprint(student_controller, url_prefix='/student')
    application.register_blueprint(teacher_controller, url_prefix='/teacher')

@application.route('/signup')
def signup():
    """
    """
    token = None # Retrieve.
    # TODO : Check if token is valid.
    return github_client.authorize()

@application.route('/token')
@github_client.authorized_handler
def authorized(oauth_token):
    """
    :param oauth_token:
    """
    next_url = request.args.get('next') or url_for('index')
    if oauth_token is None:
        flash("Authorization failed.")
        return redirect(next_url)
    user = User.query.filter_by(token=oauth_token).first()
    if user is None:
        user = User()
        user.token = oauth_token
        db_session.add(user)
    user.oauth_token = oauth_token
    db_session.commit()
    return redirect(next_url)

@github_client.access_token_getter
def token_getter():
    user = g.user
    if user is not None:
        return user.oauth_token
        
if __name__ == '__main__':
    # TODO : Get debug from env ?
    application.run(debug=True)