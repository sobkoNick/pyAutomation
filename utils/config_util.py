import os

import jsonpickle as jsonpickle

import settings
from settings import PROJECT_ROOT

json_file = os.path.join(PROJECT_ROOT, "config/{}_config.json".format(settings.ENV))
with open(json_file) as jfile:
    jsonList = jsonpickle.decode(jfile.read())


def get_config(property_to_get):
    return jsonList[property_to_get]
