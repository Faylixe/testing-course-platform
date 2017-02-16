#!/usr/bin/python

from model import database as sql

class UserExercice(sql.Model):
    """ User exercice ORM class. """

    __tablename__ = 'user_exercices'
    exercice_id = sql.Column(sql.Integer,  sql.ForeignKey('exercice.id'), primary_key=True)
    exercice = sql.relationship('Exercice', backref=sql.backref('user_exercices', lazy='dynamic'))
    github_id = sql.Column(sql.Integer, sql.ForeignKey('users.github_id'), primary_key=True)
    user = sql.relationship('User', backref=sql.backref('user_exercices', lazy='dynamic'))
    status = sql.Column(sql.Integer)
    score = sql.Column(sql.Integer)

    LOCKED = 0

    UNLOCKED = 1

    VALIDATING = 2

    VALIDATED = 3
