from flask import request
from flask.views import MethodView
from api.utils.request import parse_request
from .parser import parser
from celery import Celery
from celeryconfig import broker_url

class CreateUserView(MethodView):

  def __init__(self) -> None:
    super().__init__()

  @parse_request(request, parser)
  def post(self, request):
    celery = Celery(broker=broker_url)
    celery.send_task('create-user', args=[request])
    return {'status': 'User will be created'}
