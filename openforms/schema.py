import logging, json
from flask import request
from flask_restful import Resource
from marshmallow import Schema, fields

class ResponseSchema(Schema):
    status = fields.Str(default='success')
    msg = fields.Str(default='')

class LoginAPISchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)

class FormAPISchema(Schema):
    form = fields.String(required=True)

class AnswerAPISchema(Schema):
    sr_no = fields.Int(required=True)
    answer = fields.String(required=True)

class QuestionAPISchema(Schema):
    sr_no = fields.Int(required=True)
    title = fields.String(required=True)
    type = fields.String(required=True)
    options = fields.String(required=True)

class IntegrationsAPISchema(Schema):
    google_sheet_sync = fields.String(required=True)

class MetadataAPISchema(Schema):
    integrations = fields.Nested(IntegrationsAPISchema)

class FormAnswersAPISchema(Schema):
    answers = fields.Nested(AnswerAPISchema, many=True)
    form = fields.String(required=True)

class FormQuestionsAPISchema(Schema):
    questions = fields.Nested(QuestionAPISchema, many=True)
    description = fields.String(required=True)
    title = fields.String(required=True)
    metadata = fields.Nested(MetadataAPISchema, many=True)
