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
    MONGODB_SETTINGS = {
        "db": "oforms",
        "host": "localhost",
        "port": 27017,
        "authentication_source": "admin",
        "username": "admin",
        "password": "rahpal399",
    }

    #OAuth 
    GOOGLE_CLIENT_ID = "17066300109-7chsvo40lvra1gtln567j34247ptndla.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET = "Xrhb1l_SWoWz2RVXkCg8eiUm"
