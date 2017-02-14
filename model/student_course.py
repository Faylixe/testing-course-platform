#!/usr/bin/python

from __init__ import database as sql

class StudentCourse(sql.Model):
    """ StudentCourses ORM class. """

    # Associated table name.
    __tablename__ = 'student_courses'

    # Associated teacher id.
    course_id = sql.Column(sql.Integer, sql.ForeignKey('courses.id'))

    # Associated teacher id.
    student_id = sql.Column(sql.Integer, sql.ForeignKey('users.id'))

    # TODO : Composite primary key (student / course)
    
    # Associated course instance.
    course = sql.relationship('Course', backref=sql.backref('student_courses', lazy='dynamic'))
    
    # Associated student instance.
    student = sql.relationship('User', backref=sql.backref('student_courses', lazy='dynamic')
