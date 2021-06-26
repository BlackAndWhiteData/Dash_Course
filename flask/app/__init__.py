from flask import Flask
from importlib import import_module


def register_blueprints(app):
    module = import_module('app.home.routes')
    app.register_blueprint(module.blueprint)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints(app)

    return app