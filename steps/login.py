import requests

from utils.config_util import get_config


class LoginSteps:
    def __init__(self):
        self.logger = None

    @staticmethod
    def get_jwt():
        api_token_key = "api_token"
        token = get_config("%s" % api_token_key)
        url = get_config("base_url") + get_config("login_url")
        response = requests.post(url=url, params=[(api_token_key, token)])
        return response.json()["jwt"]
