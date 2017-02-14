#!/usr/bin/python

from __init__ import database as sql

class User(sql.Model):
    """ User ORM class. """

    # Associated table name.
    __tablename__ = 'users'

    # User identifier.
    id = sql.Column(sql.Integer, primary_key=True)

    # User type (0 for registered or 1 for facebook)
    type = sql.Column(sql.Integer)

    # First name.
    name = sql.Column(sql.String(20))

    # Password hash is not facebook type.
    token = sql.Column(sql.String(32))

    # User repository.
    repository = sql.Column(sql.String(100))
