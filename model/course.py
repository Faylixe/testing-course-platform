#!/usr/bin/python

from __init__ import database as sql

class Course(sql.Model):
    """ Courses ORM class. """

    # Associated table name.
    __tablename__ = 'courses'

    # User identifier.
    id = sql.Column(sql.Integer, primary_key=True)

    # Course name.
    name = sql.Column(sql.String(30))

    # Course key.
    key = sql.Column(sql.String(32))

    # Associated teacher id.
    teacher_id = sql.Column(sql.Integer, sql.ForeignKey('users.id'))

    # Associated teacher instance.
    teacher = sql.relationship('User', backref=sql.backref('addresses', lazy='dynamic'))