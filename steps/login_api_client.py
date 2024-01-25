import requests
from requests import Response

from steps.api_client import ApiClient
from utils.config_util import get_config


class LoginApiClient(ApiClient):
    def __init__(self):
        super().__init__()
        self.logger = None

    def get_jwt(self) -> Response:
        api_token_key = "api_token"
        token = get_config(api_token_key)
        url = get_config("base_url") + get_config("login_url")

        response = requests.post(url=url, params=[(api_token_key, token)])
        self.response = response
        return response

    def send_jwt_request(self):
        self.get_jwt()
        return self
