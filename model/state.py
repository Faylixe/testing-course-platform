#!/usr/bin/python

from model import database as sql

class PlatformState(sql.Model):
    """ Plateform state ORM class. """

    # Associated table name.
    __tablename__ = 'plateform_state'

    # Key.
    key = sql.Column(sql.String(30), primary_key=True)

    # Value.
    value = sql.Column(sql.String(30))

    def __init__(key):
        """
        """
        self.key = key
        self.value = ''

    @staticmethod
    def has(key):
        """
        :param key:
        :returns:
        """
        state = PlatformState.query.filter_by(key=key).first()
        return state is not None

    @staticmethod
    def get(key):
        """
        :param key:
        :returns:
        """
        state = PlatformState.query.filter_by(key=key).first()
        if state is not None:
            return state.value

    @staticmethod
    def put(key, value):
        """
        :param key:
        :param value:
        """
        state = PlatformState.query.filter_by(key=key).first()
        if state is None:
            state = PlatformState(key)
        state.value = value
        sql.add(state)
        sql.commit()