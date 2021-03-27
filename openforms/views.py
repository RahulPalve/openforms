import logging
from flask import request
from flask_restful import Resource
from openforms.models import User, Form, Question

logger = logging.getLogger(__name__)

class FormAPI(Resource):
    def post(self):
        data = request.json
        form = Form(**data)
        form.owner = User.objects.first() #change
        form.save()

        logger.info(data)

        return {"status": data}


