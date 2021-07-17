import logging
from flask import request
from flask_restful import Resource
from openforms.models import User, Form, Question
from openforms.auth.utils import get_jwt, login_required

logger = logging.getLogger(__name__)


class MasterFormAPI(Resource):
    """
    Master API for forms used only once while creating new form
    """
    @login_required
    def post(self, **kwargs):
        data = request.json
        form = Form(**data)
        form.owner = User.objects.get(id=kwargs["user"])
        form.save()

        logger.info(data)

        return {"status": data}

class FormAPI(Resource):
    def get(self, **kwargs):
        try: 
            form = Form.objects.get(codename=kwargs["codename"])

            if form == None:
                raise Exception("Form not found!")

            data = {
                "created_at": str(form.created_at),
                "title": form.title,
                "description": form.description,
                "questions": str(form.questions)
            }

            return {"status": "success", "data":data}

        except Exception as e:
            return {"status": "error", "msg": str(e)}       

class LoginAPI(Resource):
    def post(self):
        data = request.json

        try:
            user = User.objects.get(email=str(data["email"]), password=str(data["password"]))

        except User.DoesNotExist:
            return {"status": "error", "msg": "Invalid Credentials, User not found!"}

        return {"status": "success", "token": get_jwt(str(user.id))}
