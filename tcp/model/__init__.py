#!/usr/bin/python

from flask_sqlalchemy import SQLAlchemy

# Database instance.
database = SQLAlchemy()

def configure_database(application):
    """
    :param application:
    """
    from model.state import PlatformState
    from model.user import User
    database.init_app(application)
    #database.drop_all()
    database.create_all()
    database.session.commit()
