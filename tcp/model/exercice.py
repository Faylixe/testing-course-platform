#!/usr/bin/python

from model import database as sql

class Exercice(sql.Model):
    """ Exercice ORM class. """

    __tablename__ = 'exercices'
    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(100))
    description = sql.Column(sql.Text)
    max_score = sql.Column(sql.Integer)
