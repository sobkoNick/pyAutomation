
from copy import copy

import pytest

import settings
from fixture.application import Application
from utils import config_util

#  getting environment argument
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

    return fixture
