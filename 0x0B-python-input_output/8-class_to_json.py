#!/usr/bin/python3

"""
The module contains a function that serializes a class
"""


def class_to_json(obj):
    """
    The function that serializes a class to json
    """
    return obj.__dict__
