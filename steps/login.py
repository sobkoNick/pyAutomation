import requests

import steps.api_steps
from steps.api_steps import ApiSteps
from utils.config_util import get_config


class LoginSteps(ApiSteps):
    def __init__(self):
        super().__init__()
        self.logger = None

    # should be used in beforeClass fixture
    def get_jwt(self):
        api_token_key = "api_token"
        token = get_config("%s" % api_token_key)
        url = get_config("base_url") + get_config("login_url")
        response = requests.post(url=url, params=[(api_token_key, token)])
        self.response = response
        return response.json()["jwt"]

    def send_jwt_request(self):
        self.get_jwt()
        return self
