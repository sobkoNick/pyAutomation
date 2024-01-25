from copy import copy

import pytest

import settings
from fixture.application import Application
from steps.login_api_client import LoginClient


#  getting environment argument
from utils import config_util


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="qa", help="dev or qa"
    )


@pytest.fixture(scope="session")
def app(request):
    global fixture
    fixture = Application()

    fixture.env = request.config.getoption("--env")
    settings.ENV = copy(fixture.env)
    fixture.token = request_and_verify_jwt()
    fixture.project_id = config_util.get_config("project_id")
    return fixture


def request_and_verify_jwt():
    jwt_response = LoginClient().get_jwt()
    code = jwt_response.status_code
    jwt_token = jwt_response.json()["jwt"]
    if code != 200 or not jwt_token.strip():
        pytest.skip(f"Unable to get JWT token. Status code - {code}, token - {jwt_token}")
    return jwt_token
