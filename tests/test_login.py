from steps.login_api_client import LoginClient


def test_login(app):
    LoginClient().send_jwt_request().validate().status_code_is_ok()
