from . import blueprint
from flask import render_template


@blueprint.route('/')
def index():
    return render_template('index_home.html')