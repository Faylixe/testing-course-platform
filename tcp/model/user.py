#!/usr/bin/python

from model import database as sql
from common.github import github_client

class User(sql.Model):
    """ User ORM class. """

    # Associated table name.
    __tablename__ = 'users'

    # User identifier.
    id = sql.Column(sql.Integer, primary_key=True)

    # User type (0 for teacher or 1 for student)
    type = sql.Column(sql.Integer)

    # First name.
    name = sql.Column(sql.String(20))

    # Password hash is not facebook type.
    token = sql.Column(sql.String(100))

    # User repository.
    repository = sql.Column(sql.String(100))

    #
    TEACHER = 0

    #
    STUDENT = 1

    @staticmethod
    def create(type, token):
        """
        :param type:
        :param token:
        """
        user = User()
        user.type = type
        user.token = token
        sql.session.add(user)
        sql.session.commit()
        return user
    
    @staticmethod
    def get(token):
        """
        """
        user = User.query.filter_by(token=token).first()
        if user is None:
            user = User.create(User.STUDENT, token)
            user.name = github_client.get('user')['login']
            sql.session.add(user)
            sql.session.commit()
        return user