import json
from copy import deepcopy

from _pytest.fixtures import fixture

from constants.endpoint_names import SUITES_ENDPOINT
from models.suite_model import Suite
from steps.api_client import ApiClient


@fixture(scope="module")
def default_suite(app):
    with open("tests/test_data/suite_to_post.json") as json_data:
        data = json.load(json_data)

    # creates default suite for tests
    suite = ApiClient(token=app.token, endpoint=SUITES_ENDPOINT, logger=app.logger) \
        .post(url_params=[app.project_id], new_obj=data) \
        .validate_that().status_code_is_ok().get_response_body()
    suite = Suite.build(json.dumps(suite['data']))

    # passes suite into each test method in module
    yield suite

    # deletes the default fixture after run of all test methods in module
    ApiClient(token=app.token, endpoint=SUITES_ENDPOINT, logger=app.logger) \
        .delete(url_params=[app.project_id, suite.id]).validate_that().status_code_is_ok()


def test_get_all_suites(app, default_suite):
    """
    Test gets all suites and checks that the default is present
    """
    suite = deepcopy(default_suite)
    suite.attributes.description = ""
    ApiClient(token=app.token, endpoint=SUITES_ENDPOINT, logger=app.logger) \
        .get([app.project_id]) \
        .validate_that() \
        .status_code_is_ok() \
        .body_contains(suite)


def test_get_by_id(app, default_suite):
    """
    Test gets suite by id and checks that the default suite is returned
    """
    ApiClient(token=app.token, endpoint=SUITES_ENDPOINT, logger=app.logger) \
        .get_by_id([app.project_id, default_suite.id]) \
        .validate_that() \
        .status_code_is_ok() \
        .body_equals(default_suite)


def test_intended_to_fail(app, default_suite):
    """
    A simple test that gets all suites and check that the default is present
    """
    assert False, "expected Failure"

# TODO add test for all crud operations
