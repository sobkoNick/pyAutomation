from copy import copy

import pytest
from reportportal_client import step

import settings
from constants import endpoint_names
from fixture.application import Application
from steps.login_api_client import LoginApiClient
#  getting environment argument
from utils import config_util
from utils.logger import CustomLogger


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="qa", help="dev or qa"
    )


@pytest.fixture(scope="session")
def app(request):
    global fixture
    fixture = Application()
    fixture.logger = CustomLogger().set_up(__name__)

    fixture.logger.info("Fixture starts")

    fixture.env = request.config.getoption("--env")
    settings.ENV = copy(fixture.env)
    fixture.token = request_and_verify_jwt(fixture.logger)
    fixture.project_id = config_util.get_config("project_id")
    return fixture


@step("Sends request from fixture to get jwt token")
def request_and_verify_jwt(logger):
    jwt_response = LoginApiClient(endpoint_names.LOGIN_ENDPOINT, logger).get_jwt()
    code = jwt_response.status_code
    jwt_token = jwt_response.json()["jwt"]
    if code != 200 or not jwt_token.strip():
        pytest.skip(f"Unable to get JWT token. Status code - {code}, token - {jwt_token}")
    return jwt_token
