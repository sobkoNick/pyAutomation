from steps.validator import Validator

from utils import url_maker


# Base class for all API steps classes
class ApiClient:
    def __init__(self, token="", endpoint=""):
        self.token = token
        self.endpoint = endpoint
        self.response = None
        self.logger = None

        self.post_url = None
        self.put_url = None
        self.get_url = None
        self.get_by_id_url = None
        self.delete_url = None

        self.get_urls_for_endpoint(endpoint)

    def get_urls_for_endpoint(self, endpoint):
        url_map = url_maker.get_urls(endpoint)
        self.post_url = url_map['post']
        self.put_url = url_map['put']
        self.get_url = url_map['get']
        self.get_by_id_url = url_map['get_by_id']
        self.delete_url = url_map['delete']

    # todo use json approach for configs, data to post and to verify

    def get_headers(self):
        return {"Authorization": self.token}

    def validate(self) -> Validator:
        """
        Returns validator to check response result
        :rtype: Validator
        """
        return Validator(self.response)
