from flask import Blueprint

#https://stackoverflow.com/questions/7974771/flask-blueprint-template-folder

blueprint = Blueprint(
    'info_blueprint',
    __name__,
    url_prefix='/info',
    template_folder='templates'
)