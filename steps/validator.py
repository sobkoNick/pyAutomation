import json

from requests import Response
from assertpy import assert_that


class Validator:
    def __init__(self, response: Response):
        self.response = response

    def status_code_is_ok(self):
        actual_status_code = self.response.status_code
        assert_that(actual_status_code, f"Actual status code {actual_status_code} is not 200 OK")\
            .is_equal_to(200)
        # assert actual_status_code == 200, f"Actual status code {actual_status_code} is not 200 OK"
        return self

    def body_contains(self, expected_obj):
        """
        Verifies response body with list of items contains expected_obj
        :param expected_obj: class must have static method 'build' to build actual response obj
        """
        actual_objs = []
        for obj in self.get_response_body()['data']:
            # here I get class from expected_obj and call its method build()
            actual_objs.append(expected_obj.__class__.build(json.dumps(obj)))
        assert_that(actual_objs, f"Response \n{actual_objs} \n does not contain expected \n{expected_obj}\n")\
            .is_not_empty().contains(expected_obj)
        # assert expected_obj in actual_objs, \
        #     f"Response {actual_objs} does not contain expected {expected_obj}"

    def get_response_body(self):
        return self.response.json()
