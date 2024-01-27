import json

import requests

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

    def get_headers(self):
        return {"Authorization": self.token}

    # ------- API CALLS -------

    def get(self, url_params: list):
        """
        :param url_params: a list with params to format url with
        :return: self
        """
        self.response = requests.get(url=self.get_url.format(*url_params), headers=self.get_headers())
        return self

    def get_by_id(self, url_params: list):
        """
        :param url_params: a list with params to format url with. should include id to get
        :return: self
        """
        self.response = requests.get(url=self.get_by_id_url.format(*url_params), headers=self.get_headers())
        return self

    def post(self, url_params: list, new_obj):
        """
        :param url_params: a list with params to format url with
        :param new_obj: object to be posted
        :return: self
        """
        self.response = requests.post(url=self.post_url.format(*url_params),
                                      json=new_obj,
                                      headers=self.get_headers())
        return self

    def put(self, url_params: list, obj):
        """
        :param url_params: a list with params to format url with. should include id to update
        :param obj: object to be updated
        :return: self
        """
        self.response = requests.put(url=self.put_url.format(*url_params),
                                     json=obj,
                                     headers=self.get_headers())
        return self

    def delete(self, url_params: list):
        """
        :param url_params: a list with params to format url with. should include id to delete
        :return: self
        """
        self.response = requests.delete(url=self.delete_url.format(*url_params), headers=self.get_headers())
        return self

    def get_response_body(self):
        return self.response.json()

    def validate_that(self) -> Validator:
        """
        Returns validator to check response result
        :rtype: Validator
        """
        return Validator(self.response)
