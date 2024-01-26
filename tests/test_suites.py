from constants.endpoint_names import SUITES_ENDPOINT
from steps.api_client import ApiClient


def test_get_all_suites(app):
    ApiClient(token=app.token, endpoint=SUITES_ENDPOINT) \
        .get([app.project_id]) \
        .validate_that() \
        .status_code_is_ok()
