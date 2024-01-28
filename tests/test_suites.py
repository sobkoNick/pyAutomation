import json
from copy import deepcopy

from _pytest.fixtures import fixture

from constants.endpoint_names import SUITES_ENDPOINT
from models.suite_model import Suite
from steps.api_client import ApiClient


# class can be deleted
class TestSuites:

    # FIXTURES

    @fixture(scope="module")
    def default_suite(self, app):
        with open("tests/test_data/default_suite_to_post.json") as json_data:
            data = json.load(json_data)

        # creates default suite for tests
        suite = ApiClient(token=app.token, endpoint=SUITES_ENDPOINT, logger=app.logger) \
            .post(url_params=[app.project_id], new_obj=data) \
            .validate_that().status_code_is_ok().get_response_body()
        suite = Suite.build(json.dumps(suite['data']))

        # passes suite into each test method in module
        yield suite

        # deletes the default suite after run of all test methods in module
        app.logger.info("Deleting default fixture after test run")
        ApiClient(token=app.token, endpoint=SUITES_ENDPOINT, logger=app.logger) \
            .delete(url_params=[app.project_id, suite.id]).validate_that().status_code_is_ok()

    @fixture(scope="module")
    def new_suite(self, app):
        with open("tests/test_data/new_suite_to_post.json") as json_data:
            suite = json.load(json_data)

        # passes suite into each test method in module
        yield suite

        # deletes created suite after run of all test methods in module
        app.logger.info("Deleting created during test fixture after test run")
        ApiClient(token=app.token, endpoint=SUITES_ENDPOINT, logger=app.logger) \
            .delete(url_params=[app.project_id, suite['data']['id']]).validate_that().status_code_is_ok()

    # TESTS
    def test_get_all_suites(self, app, default_suite):
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

    def test_get_by_id(self, app, default_suite):
        """
        Test gets suite by id and checks that the default suite is returned
        """
        ApiClient(token=app.token, endpoint=SUITES_ENDPOINT, logger=app.logger) \
            .get_by_id([app.project_id, default_suite.id]) \
            .validate_that() \
            .status_code_is_ok() \
            .body_equals(default_suite)

    def test_post(self, app, new_suite):
        """
        Test posts suite and checks that that created suite is returned
        """
        post_result = ApiClient(token=app.token, endpoint=SUITES_ENDPOINT, logger=app.logger) \
            .post([app.project_id], new_suite)

        new_suite['data']['id'] = post_result.get_response_body()['data']['id']
        post_result \
            .validate_that() \
            .status_code_is_ok() \
            .body_equals(Suite.build(json.dumps(new_suite)))

    def test_intended_to_fail(self, app, default_suite):
        """
        A simple test that fails for the report
        """
        assert False, "expected Failure"
