import os
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec import FlaskApiSpec
from celery import Celery
from .tasks import make_celery
from .config import configs

env = os.environ.get("FLASK_ENV", "development")
db = MongoEngine()
rest_api = Api()
docs = FlaskApiSpec()
celery = Celery(
    __name__, broker=configs[env].CELERY_BROKER_URL, backend=configs[env].CELERY_RESULT_BACKEND
)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configs[env])
    app.config.update({
            'APISPEC_SPEC': APISpec(
                title='openforms',
                version='v1',
                openapi_version='2.0',
                plugins=[MarshmallowPlugin()],
            ),
            'APISPEC_SWAGGER_URL': '/swagger/',
            'APISPEC_SWAGGER_UI_URL': '/docs/',
        })
    register_extensions(app)
    global celery
    celery = make_celery(app)
    return app


def register_extensions(app):
    db.init_app(app)
    rest_api.init_app(app)
    docs.init_app(app)


from .routes import *  # set url routes
