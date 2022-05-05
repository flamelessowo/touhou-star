import json


def read_config(path_to_config, key=None):
    with open(path_to_config) as f:
        constants = json.load(f)
        return constants[key] if key else constants
