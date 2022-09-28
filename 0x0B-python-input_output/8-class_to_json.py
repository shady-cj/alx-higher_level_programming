#!/usr/bin/python3

"""
The module contains a function that serializes a class
"""
import json



class EncodeClass(json.JSONEncoder):
    """
    encodes the class by returning a dictionary of the class object
    """
    def default(self, obj):
        return obj.__dict__


def class_to_json(obj):
    """
    The function that serializes a class to json
    """
    return json.loads(json.dumps(obj, cls=EncodeClass))
