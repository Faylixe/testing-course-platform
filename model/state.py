#!/usr/bin/python

from __init__ import database as sql

# Consider using datastore ?

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
    def get(key):
        """
        :param key:
        :returns:
        """
        state = PlateformState.query.filter_by(key=key).first()
        if state is not None:
            return state.value

    @staticmethod
    def put(key, value):
        """
        :param key:
        :param value:
        """
        state = PlateformState.query.filter_by(key=key).first()
        if state is None:
            state = PlateformState(key)
        state.value = value
        sql.add(state)
        sql.commit()