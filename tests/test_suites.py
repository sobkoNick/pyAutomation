import json

from _pytest.fixtures import fixture

from constants.endpoint_names import SUITES_ENDPOINT
from models.suite_model import Suite
from steps.api_client import ApiClient


@fixture(scope="module")
def default_suite(app):
    with open("tests/test_data/suite_to_post.json") as json_data:
        data = json.load(json_data)

    # creates default suite for tests
    suite = ApiClient(token=app.token, endpoint=SUITES_ENDPOINT) \
        .post(url_params=[app.project_id], new_obj=data) \
        .validate_that().status_code_is_ok().get_response_body()
    suite = Suite.build(json.dumps(suite['data']))
    suite.attributes.description = ""

    # passes suite into each test method in module
    yield suite

    # deletes the default fixture after run of all test methods in module
    ApiClient(token=app.token, endpoint=SUITES_ENDPOINT) \
        .delete(url_params=[app.project_id, suite.id]).validate_that().status_code_is_ok()


def test_get_all_suites(app, default_suite):
    ApiClient(token=app.token, endpoint=SUITES_ENDPOINT) \
        .get([app.project_id]) \
        .validate_that() \
        .status_code_is_ok() \
        .body_contains(default_suite)

# TODO add test for all crud operations
