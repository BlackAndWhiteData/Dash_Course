from flask import Flask
from importlib import import_module
from .dashboards.dash_layout import dashboard_1


def register_blueprints(app):

    for blueprint_name in ('home','info','base','dashboards'):
        module = import_module('app.{}.routes'.format(blueprint_name))
        app.register_blueprint(module.blueprint)


def create_app(config):
    app = Flask(__name__,template_folder='./base/templates', static_folder='./base/static')
    app.config.from_object(config)
    register_blueprints(app)
    app = dashboard_1.Add_Dash(app)

    return app