from openforms import rest_api
from .views import MasterFormAPI, FormAPI, LoginAPI

rest_api.add_resource(MasterFormAPI, "/form/")
rest_api.add_resource(FormAPI, "/form/<string:codename>")
rest_api.add_resource(LoginAPI, "/login/")
