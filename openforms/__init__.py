import os
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api

db = MongoEngine()
rest_api = Api()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("openforms.config.Config")
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    rest_api.init_app(app)

import openforms.routes #set url routes

