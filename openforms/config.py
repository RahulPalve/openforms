import os


class DevelopmentConfig(object):
    """Base config class."""

    # Flask app config
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.getenv("SECRET_KEY", "changeth1s3cr3tKeyTh1si5un5@fe")

    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Site domain
    SITE_TITLE = "OpenForms"
    SITE_DOMAIN = "http://localhost:8080"

    # MongoEngine config
    MONGODB_SETTINGS = {
        "db": os.getenv("DB_NAME", "oforms"),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", 27017),
        "authentication_source": "admin",
        "username": os.getenv("DB_USERNAME", "admin"),
        "password": os.getenv("DB_PASSWORD", "rahpal399"),
    }

class ProductionConfig(object):
    """Base config class."""

    # Flask app config
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.getenv("PROD_SECRET_KEY", "changeth1s3cr3tKeyTh1si5un5@fe")

    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Site domain
    SITE_TITLE = "OpenForms"
    SITE_DOMAIN = "http://localhost:8080"

    # MongoEngine config
    MONGODB_SETTINGS = {
        "db": os.getenv("PROD_DB_NAME", "oforms"),
        "host": os.getenv("PROD_DB_HOST", "localhost"),
        "port": os.getenv("PROD_DB_PORT", 27017),
        "authentication_source": "admin",
        "username": os.getenv("PROD_DB_USERNAME", "admin"),
        "password": os.getenv("PROD_DB_PASSWORD", "rahpal399"),
    }

configs = {
    "development" : DevlopmentConfig,
    "production" : ProductionConfig
}
