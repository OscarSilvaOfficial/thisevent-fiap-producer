import pytest
from api import application 

class TestViews:

  @pytest.fixture(scope='module')
  def app(self):
    return application() 

  def test_create_user_view(self, app):
    user = {
      'name': 'Oscar',
      'email': 'qq@qq.com',
      'password': '123'
    }
    app.test_client().post('api/users', json=user)
