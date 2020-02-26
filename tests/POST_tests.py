import pytest
import json
from common.api_helper import ApiHelper
from common.utils import Utils
from model.user import User

api_helper = ApiHelper()
user = User()
utils = Utils()


class TestPostRequest:
    
    def test_create_new_user(self, user_endpoint):
        new_user_data = user.random_user()
        resp = api_helper.send_post_request(user_endpoint, new_user_data)
        parsed_resp = utils.paser_json(resp.text)
        assert resp.status_code == 201, resp.text
        assert parsed_resp['first_name'] == new_user_data['first_name'], resp.text
        assert parsed_resp['job'] == new_user_data['job'], resp.text
