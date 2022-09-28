#!/usr/bin/python3

"""
This module contains a function that
deserialize a json object
"""
import json


def from_json_string(my_obj):
    """ The function deserializes my_obj """
    return json.loads(my_obj)
