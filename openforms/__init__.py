import os

from flask import Flask
from flask_pymongo import PyMongo
import openforms.views


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("openforms.config.Config")

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app):
    app.register_blueprint(views.root)


def register_extensions(app):
    db = PyMongo(app)
