from constants.endpoint_names import LOGIN_ENDPOINT
from steps.login_api_client import LoginApiClient


def test_login(app):
    LoginApiClient(LOGIN_ENDPOINT)\
        .send_jwt_request()\
        .validate_that()\
        .status_code_is_ok()
