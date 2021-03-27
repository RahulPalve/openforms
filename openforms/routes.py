from openforms import rest_api
from .views import FormAPI

rest_api.add_resource(FormAPI,"/form/")