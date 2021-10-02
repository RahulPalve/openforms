from openforms import rest_api
from .views import MasterFormAPI, FormAPI, LoginAPI, ResponseAPI, MasterResponseAPI

rest_api.add_resource(MasterFormAPI, "/form/")
rest_api.add_resource(FormAPI, "/form/<string:codename>")
rest_api.add_resource(LoginAPI, "/login/")
rest_api.add_resource(MasterResponseAPI, "/response/")
rest_api.add_resource(ResponseAPI, "/response/<string:form>")
