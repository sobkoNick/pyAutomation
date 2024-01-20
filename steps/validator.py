from requests import Response


class Validator:
    def __init__(self, response: Response):
        self.response = response

    def status_code_is_ok(self):
        actual_status_code = self.response.status_code
        assert actual_status_code == 200, f"Actual status code {actual_status_code} is not 200 OK"
