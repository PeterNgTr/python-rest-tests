import pytest
from common.api_helper import ApiHelper
from common.utils import Utils

api_helper = ApiHelper()
utils = Utils()

class TestGetRequest:

    @pytest.mark.parametrize("user_id, first_name", [(1, "George"), (2, "Janet")])
    def test_get_valid_user(self, user_endpoint, user_id, first_name):
        url = user_endpoint + str(user_id)
        resp = api_helper.send_get_request(url)
        parsed_resp = utils.paser_json(resp.text)
        assert resp.status_code == 200, resp.text
        assert parsed_resp['data']['id'] == user_id, resp.text
        assert parsed_resp['data']['first_name'] == first_name, resp.text

    def test_get_invalid_user(self, user_endpoint):
        url = f'{user_endpoint}100'
        resp = api_helper.send_get_request(url)
        assert resp.status_code == 404, resp.text
