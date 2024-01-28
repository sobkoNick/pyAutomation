import logging

from reportportal_client import RPLogger


class CustomLogger:
    def __init__(self):
        self.logger = None

    def set_up(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # console logger
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.INFO)
        logger.addHandler(stream_handler)

        # RP logger
        logger.setLevel(logging.DEBUG)
        logging.setLoggerClass(RPLogger)

        self.logger = logger
        return self.logger

    def log_request_parameters(self, type_of_request, url, headers, body):
        self.logger.info("%s url = %s" % (type_of_request, url))
        self.logger.info("%s header = %s" % (type_of_request, headers))
        self.logger.info("%s body = %s" % (type_of_request, body))

    def log_response(self, response):
        self.logger.info("Response code = %s" % response.status_code)
        self.logger.info("Response text = %s" % response.text)
