from steps.login import LoginSteps


def test_login(app):
    LoginSteps().send_jwt_request().validate().status_code_is_ok()
