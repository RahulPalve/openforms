from flask_restful import Resource
from openforms.models import User, Form, Question

class FormAPI(Resource):
    def get(self):
        return {"status":"success"}


