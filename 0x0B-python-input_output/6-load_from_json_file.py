#!/usr/bin/python3

"""
This module contains a function that
deserialize a json file
"""
import json


def load_from_json_file(filename):
    """ The function jsonifies my_obj and writes into
    filename
    """
    obj = None
    with open(filename, "r") as f:
        obj = json.load(f)
    return obj
