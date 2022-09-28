#!/usr/bin/python3

"""
This module contains a function that
jsonify a string
"""
import json


def to_json_string(my_obj):
    """ The function jsonifies my_obj """
    return json.dumps(my_obj)
