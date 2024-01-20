from steps.validator import Validator


# Base class for all API steps classes
class ApiSteps:
    def __init__(self):
        self.response = None

    def validate(self) -> Validator:
        """
        Returns validator to check response result
        :rtype: Validator
        """
        return Validator(self.response)
