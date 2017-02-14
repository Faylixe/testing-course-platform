#!/usr/bin/python

from os import environ as env
from flask import Flask
from flask.ext.github import GitHub
from controller.setup import is_setup, controller as setup_controller
from controller.teacher import controller as teacher_controller
from controller.student import controller as student_controller

# Application creation / configuration.
application = Flask(__name__)
application.secret_key = env['APPLICATION_SECRET_KEY']
application.config['GITHUB_CLIENT_ID'] = env['GITHUB_CLIENT_ID']
application.config['GITHUB_CLIENT_SECRET'] = env['GITHUB_CLIENT_SECRET']
application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

# Registers application controllers.
application.register_blueprint(setup_controller, url_prefix='/setup')
if is_setup():
    application.register_blueprint(student_controller, url_prefix='/student')
    application.register_blueprint(teacher_controller, url_prefix='/teacher')

# Database intialization.
database.init_app(application)

# Github client initialization.
github = GitHub(application)

if __name__ == '__main__':
    # TODO : Get debug from env ?
    application.run(debug=True)