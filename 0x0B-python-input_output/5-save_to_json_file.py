#!/usr/bin/python3

"""
This module contains a function that
jsonify a string and write it to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """ The function jsonifies my_obj and writes into
    filename
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
