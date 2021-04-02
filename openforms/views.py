import logging
from flask import request
from flask_restful import Resource
from openforms.models import User, Form, Question
from openforms.auth.utils import get_jwt, login_required
logger = logging.getLogger(__name__)

class FormAPI(Resource):

    @login_required
    def post(self,**kwargs):
        data = request.json
        form = Form(**data)
        form.owner = User.objects.get(id=kwargs["user"])
        form.save()

        logger.info(data)

        return {"status": data}

class LoginAPI(Resource):
     def post(self):
        data = request.json

        try:
            user = User.objects.get(email=data["email"], password=data["password"])
            
        except User.DoesNotExist:
            return{
                "status":"error",
                "msg":"Invalid Credentials, User not found!"
            }
        
        return {    
            "status":"success",
            "token": get_jwt(str(user.id))
            }

