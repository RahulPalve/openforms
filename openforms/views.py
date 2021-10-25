import logging, json
from flask import request
from flask_restful import Resource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from .models import Response, User, Form, Question
from .auth.utils import get_jwt, login_required
from .response_validator import ValidateResponse
from .tasks import tasks
from . import docs

logger = logging.getLogger(__name__)


class MasterFormAPI(MethodResource, Resource):
    """
    Master API for forms used only once while creating new form
    """

    @doc(description='Create form', tags=['login required', 'POST', 'All'])
    @login_required
    def post(self, **kwargs):
        data = request.json
        form = Form(**data)
        form.owner = User.objects.get(id=kwargs["user"])
        form.save()

        logger.info(data)

        return {"status": form.codename}

docs.register(MasterFormAPI)

class FormAPI(MethodResource, Resource):
    @doc(description='Get form', tags=['GET', 'All'])
    def get(self, **kwargs):
        try:
            form = Form.objects.get(codename=kwargs["codename"])

            if form == None:
                raise Exception("Form not found!")

            return {"status": "success", "data": json.loads(form.to_json())}

        except Exception as e:
            return {"status": "error", "msg": str(e)}

docs.register(FormAPI)

class MasterResponseAPI(MethodResource, Resource):
    @doc(description='Answer form', tags=['login required', 'POST', 'All'])
    @login_required
    def post(self, **kwargs):
        data = request.json
        print(data)
        user = User.objects.get(id=kwargs["user"])
        form = Form.objects.get(codename=data["form"])

        try:
            Response.objects.get(form=form, user=user)
            return {"status": "error", "msg": "Form is already filled by the user!"}

        except Response.DoesNotExist:
            validated_data = ValidateResponse(data["answers"], form)

            if validated_data.is_valid():
                ans = Response(user=user, form=form, answers=data["answers"])
                ans.save()
                return {"status": "success"}
            else:
                return {"status": "error", "msg": validated_data.errors}

docs.register(MasterResponseAPI)

class ResponseAPI(MethodResource, Resource):
    @doc(description='Get Answer', tags=['login required', 'GET', 'All'])
    @login_required
    def get(self, **kwargs):
        try:
            form = Form.objects.get(codename=kwargs["form"])
            user = User.objects.get(id=kwargs["user"])
            ans = Response.objects.get(form=form, user=user).to_json()
            ans = json.loads(ans)
            resp = {"form": form.codename, "answers": ans.get("answers")}
            return {"status": "success", "data": resp}

        except Exception as e:
            return {"status": "error", "msg": str(e)}

docs.register(ResponseAPI)

class LoginAPI(MethodResource, Resource):
    @doc(description='Login', tags=['POST', 'All'])
    def post(self, **kwargs):
        data = request.json
        try:
            user = User.objects.get(email=str(data["email"]), password=str(data["password"]))

        except User.DoesNotExist:
            return {"status": "error", "msg": "Invalid Credentials, User not found!"}
        except Exception as e:
            return {"status": "error", "msg": str(e)}

        return {"status": "success", "msg": get_jwt(str(user.id))}
docs.register(LoginAPI)
