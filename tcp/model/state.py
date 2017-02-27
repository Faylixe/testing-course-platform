#!/usr/bin/python

from model import database as sql

TEACHER_KEY = 'setup_teacher'

REPOSITORY_KEY = 'setup_repository'

class PlatformState(sql.Model):
    """ Plateform state ORM class. """

    # Associated table name.
    __tablename__ = 'platform_state'

    # Key.
    key = sql.Column(sql.String(30), primary_key=True)

    # Value.
    value = sql.Column(sql.String(30))

    def __init__(self, key):
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
        sql.session.add(state)
        sql.session.commit()

class StateCache(object):
    """Holder for the PlatformState value.
    
    Allows to only query database once to retrieve state value
    and acts as value cache after first queried.
    """

    def __init__(self, key):
        """Default constructor.
        
        :param key: Key of the value to hold.
        """
        self.key = key
        self.value = None
    
    def get_value(self):
        """
        :returns:
        """
        if self.value is None:
            self.value = PlatformState.get(self.key)
        return self.value

    def set_value(self, value):
        """
        """
        self.value = value
        PlatformState.put(self.key, value)