import os
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api
from authlib.integrations.flask_client import OAuth

# services instanciated to avoid circular import
# later registered in 'register_extensions' func
db = MongoEngine()
oauth = OAuth()
rest_api = Api()

import openforms.views

app = Flask(__name__, instance_relative_config=True)

def create_app(test_config=None):
    # create and configure the app
    app.config.from_object("openforms.config.Config")

    register_blueprints(app)
    register_extensions(app)
    return app


def register_blueprints(app):
    app.register_blueprint(views.root)


def register_extensions(app):
    db.init_app(app)
    oauth.init_app(app)
    rest_api.init_app(app)
    rest_api.add_resource(views.FormAPI, "/")


# google_auth = oauth.register(
#     name="google",
#     client_id=app.config.get("GOOGLE_CLIENT_ID"),
#     client_secret=app.config.get("GOOGLE_CLIENT_SECRET"),
#     access_token_url="https://accounts.google.com/o/oauth2/token",
#     access_token_params=None,
#     authorize_url="https://accounts.google.com/o/oauth2/auth",
#     authorize_params=None,
#     api_base_url="https://www.googleapis.com/oauth2/v1/",
#     userinfo_endpoint="https://openidconnect.googleapis.com/v1/userinfo",  # This is only needed if using openId to fetch user info
#     client_kwargs={"scope": "openid email profile"},
# )