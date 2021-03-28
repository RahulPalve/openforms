import logging
from flask import request
from flask_restful import Resource
from openforms.models import User, Form, Question
from openforms.auth.utils import get_jwt, login_required
logger = logging.getLogger(__name__)

class FormAPI(Resource):
    def get(self):
        return {"token": get_jwt("60436ca8af409d4dea3acf24")}

    @login_required
    def post(self,**kwargs):
        data = request.json
        form = Form(**data)
        form.owner = User.objects(id=kwargs["user"]).first()
        form.save()

        logger.info(data)

        return {"status": data}


