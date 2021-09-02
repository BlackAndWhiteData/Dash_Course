from flask import Blueprint

blueprint = Blueprint(
    'dashboards_blueprint',
    __name__,
    url_prefix='/dashboards',
    template_folder='templates'
)