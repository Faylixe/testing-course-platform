#!/usr/bin/python

from __init__ import database as sql

# Consider using datastore ?

class PlateformState(sql.Model):
    """ Plateform state ORM class. """

    # Associated table name.
    __tablename__ = 'plateform_state'

    # User identifier.
    id = sql.Column(sql.Integer, primary_key=True)

    # Course name.
    key = sql.Column(sql.String(30))

    # Associated teacher id.
    value = sql.Column(sql.Integer, sql.ForeignKey('users.id'))

    # Associated teacher instance.
    teacher = sql.relationship('User', backref=sql.backref('addresses', lazy='dynamic'))