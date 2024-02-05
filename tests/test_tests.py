import pytest

from steps.test_enpoint_steps import TestEndpointClient


@pytest.mark.skip(reason="Unfinished test")
def test_get_all_test(app):
    # TODO Redo after testing suites
    TestEndpointClient(app.token) \
        .get_all_tests(app.project_id) \
        .validate_that() \
        .status_code_is_ok()
