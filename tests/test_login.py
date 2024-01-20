import unittest

from steps.login import LoginSteps


class TestLogin(unittest.TestCase):

    def test_login(self):
        LoginSteps().send_jwt_request().validate().status_code_is_ok()

