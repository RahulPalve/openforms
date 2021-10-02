import datetime, uuid
from mongoengine import signals
from openforms import db
from openforms import celery


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
        "date": "Date",
        "time": "Time",
    }
    type = db.StringField(max_length=8, choices=ANS_TYPE.keys(), required=True)
    options = db.ListField(db.StringField())


class Form(db.Document):
    codename = db.StringField(default=lambda: str(uuid.uuid4()))
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    title = db.StringField(required=True)
    description = db.StringField()
    owner = db.ReferenceField(User)  # consider LazyReferenceField
    questions = db.EmbeddedDocumentListField(Question)
    metadata = db.DictField()


class Answer(db.EmbeddedDocument):
    sr_no = db.IntField()
    answer = db.StringField()


class Response(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    form = db.ReferenceField(Form)
    user = db.ReferenceField(User)
    answers = db.EmbeddedDocumentListField(Answer)

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        print("In response post save")
        integrations = document.form.metadata.get("integrations")
        if integrations:
            for task in integrations.keys():
                integrations[task]["response_id"] = str(document.id)
                print(integrations[task])
                print(integrations)
                celery.send_task(name=task, kwargs=integrations[task])


signals.post_save.connect(Response.post_save, sender=Response)
