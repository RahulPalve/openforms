# openforms API
Online forms for data collection, supports integration with google sheets. Built Using Flask, MongoDB and Celery.  

checkout UI for this API@[Openforms Frontend](https://github.com/RahulPalve/openforms-frontend)

### Tools Used:

* Python 3.8.0
* Flask 
* MongoEngine with MongoDB
* Celery 
* Redis as task queue
* docker-compose
* Pyenv for package management
* JWT for auth

### Setup Intructions:

    docker-compose up

use python 3.8.0 venv recommended

    pip install -r requirements.py

    python setup_user.py

    export FLASK_APP="openforms"

    flask run
    celery -A openforms.celery worker -l info

Use loginAPI to get JWT token,
send Authorisation: JWT {token} in header for other requests.

use below link to get postman collection for API,
https://www.getpostman.com/collections/469a937c54ea1cafafa2

postman documentation
https://documenter.getpostman.com/view/13321004/TzsYPV2k

**for google sheets integration**
openforms/integrations/google_sheets/credentials.json is needed, gcloud service account json.

make sure sheet_id provided in form should be accessible to service account used.


### Approach
**How integration with google sheets work?**
On every form, a metadata field is defined. this metadata is processed on post_save signal of response. Multiple integrations can be performed in a generalised way. this metadata contain a celery task name as key and other necessary data for that integration as value. As celery task is performed asynchronously, this does not affect performance of view and heavy tasks can be performed. Integrations can be plugged when required with metadata.

### features

 - Response by user is validated at backend with ValidateResponse class.
 -  implemented login_required decorator which is used provide stateless auth.