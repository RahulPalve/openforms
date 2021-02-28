import os


class Config(object):
    """Base config class."""

    # Flask app config
    DEBUG = True
    TESTING = True
    SECRET_KEY = "changeth1s3cr3tKey"
    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # Site domain
    SITE_TITLE = "OpenForms"
    SITE_DOMAIN = "http://localhost:8080"
    # MongoEngine config
    MONGO_URI = "mongodb://admin:rahpal399@localhost:27017/oforms"