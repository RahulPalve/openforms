from flask import Blueprint
from openforms.models import User, Form, Question

root = Blueprint("root", __name__, url_prefix="/")


@root.route("/")
def hello():
    user = User(name="John Doe", email="jb@mail.com").save()

    form = Form(title="Survey", description="covid survey", owner=user)
    question = Question(title="What?", type="TXT", description=["qwerty"])
    form.questions.append(question)
    form.save()

    return "Hello, World!"
