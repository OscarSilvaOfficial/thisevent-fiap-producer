from flask_restful import Api

from api.views.view import CreateUserView


def routes(api: Api):
  api.add_resource(CreateUserView, '/users')