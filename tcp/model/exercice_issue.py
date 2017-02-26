#!/usr/bin/python

from model import database as sql

class ExerciceIssue(sql.Model):
    """ Exercice issues issueORM class. """

    __tablename__ = 'exercice_issues'
    id = sql.Column(sql.Integer,  primary_key=True)
    exercice_id = sql.Column(sql.Integer,  sql.ForeignKey('exercices.id'), primary_key=True)
    exercice = sql.relationship('Exercice', backref=sql.backref('exercice_issues', lazy='dynamic'))
    name = sql.Column(sql.String(100))
    description = sql.Column(sql.Text)

    def __init__(self, exercice_id):
        self.id = ExerciceIssue.query.filter_by(exercice_id=exercice_id).count() # Consider using fast count. # TODO : Protect againt conflict.
        self.name = ''
        self.description = ''
