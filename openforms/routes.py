from openforms import rest_api
from .views import FormAPI, LoginAPI

rest_api.add_resource(FormAPI,"/form/")
rest_api.add_resource(LoginAPI,"/login/")
