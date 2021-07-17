import datetime, uuid
from openforms import db


class User(db.Document):
    name = db.StringField()
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)


class Question(db.EmbeddedDocument):
    sr_no = db.IntField()
    title = db.StringField(required=True)
    ANS_TYPE = {
        "text": "Text",
        "mcq": "Multiple Choice",
        "checkbox": "Checkbox",
        "dropdown": "Dropdown",
        "date": "Date",
        "time": "Time",
    }
    type = db.StringField(max_length=8, choices=ANS_TYPE.keys(), required=True)
    description = db.ListField(db.StringField())


class Form(db.Document):
    codename = db.StringField(default=str(uuid.uuid4()))
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    title = db.StringField(required=True)
    description = db.StringField()
    owner = db.ReferenceField(User)  # consider LazyReferenceField
    questions = db.EmbeddedDocumentListField(Question)

class Answer(db.Document):
    form = db.ReferenceField(Form)
    user = db.ReferenceField(User)
    answers = db.ListField(db.StringField())