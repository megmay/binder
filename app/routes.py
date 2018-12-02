""" Description """

from flask import render_template, request
from app import APP


@APP.route('/')
@APP.route('/dashboard')
def dashboard():
    """
    Returns dashboard html template
    """

    return render_template('dashboard.html')
