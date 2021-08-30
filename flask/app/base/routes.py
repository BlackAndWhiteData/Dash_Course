from . import blueprint
from flask import redirect, url_for


@blueprint.route('/')
def index():
    return redirect(url_for('home_blueprint.index'))