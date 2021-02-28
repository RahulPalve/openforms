from flask import Blueprint

root = Blueprint("root", __name__, url_prefix="/")


@root.route("/")
def hello():
    return "Hello, World!"
