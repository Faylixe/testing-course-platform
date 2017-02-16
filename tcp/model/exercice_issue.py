#!/usr/bin/python

from model import database as sql

class ExerciceIssue(sql.Model):
    """ Exercice issueORM class. """

    __tablename__ = 'exercices_issue'
    id = sql.Column(sql.Integer,  primary_key=True)
    exercice_id = sql.Column(sql.Integer,  sql.ForeignKey('exercice.id'), primary_key=True)
    exercice = sql.relationship('Exercice', backref=sql.backref('user_exercices', lazy='dynamic'))
    name = sql.Column(sql.String(100))
    description = sql.Column(sql.Text)