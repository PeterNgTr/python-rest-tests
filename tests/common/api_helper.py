import requests


class ApiHelper:

    def send_post_request(self, url, data=None, json=None, **kwargs):
            return requests.post(url, data=data, **kwargs)

    def send_get_request(self, url, params=None, **kwargs):
            return requests.get(url, params=params, **kwargs)
