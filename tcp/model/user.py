#!/usr/bin/python

from model import database as sql
from common import github_client

class User(sql.Model):
    """ User ORM class. """

    __tablename__ = 'users'
    github_id = sql.Column(sql.Integer, primary_key=True)
    type = sql.Column(sql.Integer)
    name = sql.Column(sql.String(20))
    token = sql.Column(sql.String(100))
    repository = sql.Column(sql.String(100))

    #
    TEACHER = 0

    #
    STUDENT = 1

    @staticmethod
    def create(type, github_id, token):
        """
        :param type:
        :param github_id:
        """
        user = User()
        user.github_id = github_id
        user.type = type
        user.name = github_client.get('user')['login']
        user.token = token
        sql.session.add(user)
        sql.session.commit()
        return user
    
    @staticmethod
    def get(github_id, token):
        """
        """
        created = False
        user = User.query.filter_by(github_id=github_id).first()
        if user is None:
            user = User.create(User.STUDENT, github_id, token)
            created = True
            sql.session.add(user)
            sql.session.commit()
        return user, created