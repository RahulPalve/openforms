from flask import Blueprint
from flask_restful import Resource
from openforms.models import User, Form, Question

root = Blueprint("root", __name__, url_prefix="/")

class FormAPI(Resource):
    def post(self, codename):
        pass
    def get(self):
        return {"Succuess":True}
        pass
    def patch(self, codename):
        pass
    def delete(self, codename):
        pass

@root.route("/")
def hello():
    user = User(name="John Doe", email="jb@mail.com").save()

    form = Form(title="Survey", description="covid survey", owner=user)
    question = Question(title="What?", type="TXT", description=["qwerty"])
    form.questions.append(question)
    form.save()

    return "Hello, World!"
