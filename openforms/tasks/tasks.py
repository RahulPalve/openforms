import json, os
from openforms.models import Response
from openforms import celery
from openforms.integrations.google_sheets import GoogleSheetIntegration
from openforms.config import configs
from mongoengine import connect

connect(**configs[os.environ.get("FLASK_ENV","development")].MONGODB_SETTINGS)


@celery.task(name="google_sheet_sync")
def google_sheet_sync(**kwargs):

    sheet = GoogleSheetIntegration(kwargs["sheet_id"])

    response = Response.objects.get(id=kwargs.get("response_id"))

    headers_data = ["reponse_datetime"]
    for q in response.form.questions:
        headers_data.append(q.title)

    sheet.set_header(headers_data)

    answers = json.loads(response.to_json())["answers"]
    row_data = [
        str(response.created_at),
    ]
    for ans in answers:
        row_data.append(ans["answer"])

    sheet.add_row(row_data)
