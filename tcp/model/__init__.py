#!/usr/bin/python

from flask_sqlalchemy import SQLAlchemy

# Database instance.
database = SQLAlchemy()

def configure_database(application):
    """
    :param application:
    """
    from model.exercice import Exercice
    from model.exercice_issue import ExerciceIssue
    from model.state import PlatformState
    from model.user import User
    database.init_app(application)
    database.drop_all()
    database.create_all()
    database.session.commit()
