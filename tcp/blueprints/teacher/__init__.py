#!/usr/bin/python

""" To document. """

from flask import Blueprint, render_template, request, redirect, session, url_for
from common import github_client
from common.access import get_current_user, teacher_restricted
from model import database
from model.exercice import Exercice
from model.exercice_issue import ExerciceIssue
from model.user import User

# Backend controller instance.
controller = Blueprint('teacher', __name__, template_folder='templates')

@controller.route('/dashboard')
@teacher_restricted
def dashboard():
    """ /teacher/dashboard endpoint """
    # TODO : Retrieve metadata.
    return render_template('dashboard.html', current=get_current_user())

@controller.route('/exercice')
@controller.route('/exercice/<int:exercice_id>')
@teacher_restricted
def view_exercice(exercice_id=None):
    """ /teacher/exercice endpoint

    :param exercice_id: Optional identifier of the exercice to display.
    """
    if exercice_id is not None:
        exercice = Exercice.query.filter_by(id=exercice_id).first_or_404()
        issues = ExerciceIssue.query.filter_by(exercice_id=exercice_id).all()
        return render_template('view_exercice.html', current=get_current_user(), exercice=exercice, issues=issues)
    return render_template('list_exercice.html', current=get_current_user(), exercices=Exercice.query.all())

@controller.route('/exercice/edit', methods=['GET', 'POST'])
@controller.route('/exercice/edit/<int:exercice_id>', methods=['GET', 'POST'])
@teacher_restricted
def edit_exercice(exercice_id=None):
    """ /teacher/exercice/edit endpoint
    
    :param id: Optional identifier of the exercice to edit.
    """
    exercice = Exercice()
    if exercice_id is not None:
        exercice = Exercice.query.filter_by(id=exercice_id).first_or_404()
    if request.method == 'POST':
        exercice.name = request.form.get('name')
        exercice.description = request.form.get('description')
        exercice.max_score = int(request.form.get('max_score'))
        database.session.add(exercice)
        database.session.commit()
        return redirect(url_for('.view_exercice'))
    return render_template('edit_exercice.html', current=get_current_user(), exercice=exercice)

@controller.route('/exercice/<int:exercice_id>/issue/<int:issue_id>')
@teacher_restricted
def view_issue(exercice_id, issue_id):
    """ /teacher/exercice/<exercice_id>/issue/<issue_id> endpoint

    :param id: Optional identifier of the issue to display.
    """
    issue = ExerciceIssue.query.filter_by(id=issue_id, exercice_id=exercice_id).first_or_404()
    return render_template('view_issue.html', current=get_current_user(), issue=issue)
    
@controller.route('/exercice/<int:exercice_id>/issue/edit', methods=['GET', 'POST'])
@controller.route('/exercice/<int:exercice_id>/issue/edit/<int:issue_id>', methods=['GET', 'POST'])
@teacher_restricted
def edit_issue(exercice_id, issue_id=None):
    """ /teacher/exercice/<exercice_id>/issue/edit endpoint
    
    :param id: Optional identifier of the issue to edit.
    """
    issue = ExerciceIssue()
    if issue_id is not None:
        issue = ExerciceIssue.query.filter_by(id=issue_id, exercice_id=exercice_id).first_or_404()
    if request.method == 'POST':
        # TODO : Get issue values.
        database.session.add(issue)
        database.session.commit()
        return redirect(url_for('.view_exercice', exercice_id=exercice_id))
    return render_template('edit_issue.html', current=get_current_user(), issue=issue)