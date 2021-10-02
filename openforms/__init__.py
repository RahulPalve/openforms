import os
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api
from celery import Celery
from .tasks import make_celery
from .config import configs

env = os.environ.get("FLASK_ENV", "development")
db = MongoEngine()
rest_api = Api()
celery = Celery(
    __name__, broker=configs[env].CELERY_BROKER_URL, backend=configs[env].CELERY_RESULT_BACKEND
)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configs[env])
    register_extensions(app)
    global celery
    celery = make_celery(app)
    return app


def register_extensions(app):
    db.init_app(app)
    rest_api.init_app(app)


import openforms.routes  # set url routes
