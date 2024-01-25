from steps.test_enpoint_steps import TestEndpointClient


def test_get_all_test(app):
    TestEndpointClient(app.token) \
        .get_all_tests(app.project_id) \
        .validate() \
        .status_code_is_ok()
