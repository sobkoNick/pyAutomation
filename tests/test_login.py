from constants.endpoint_names import LOGIN_ENDPOINT
from steps.login_api_client import LoginApiClient


def test_login(app):
    # TODO delete
    LoginApiClient(LOGIN_ENDPOINT, app.logger)\
        .send_jwt_request()\
        .validate_that()\
        .status_code_is_ok()
