from . import blueprint
from flask import render_template


@blueprint.route('/first')
def first():
    return render_template('dashboard_1.html')

@blueprint.route('/second')
def second():
    return render_template('dashboard_2.html')