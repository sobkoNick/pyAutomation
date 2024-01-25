import requests

from steps.api_client import ApiClient
from utils.config_util import get_config


class SuiteEndpointClient(ApiClient):
    def __init__(self, token):
        super().__init__(token)
        self.suite_url = get_config("base_url") + get_config("test_url")

    def get_all_suites(self, project_id):
        self.response = requests.get(url=self.suite_url.format(project_id), headers=self.get_headers())
        return self
