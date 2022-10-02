#!/usr/bin/python3


"""
This module defines a base class
"""
import json


class Base:

    """
    Defining the Base class with all the public
    and private attributes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Serializes list of dictionaries.
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saving a serialized list of objects into
        files
        """
        obj = []
        if list_objs is not None:
            for instance in list_objs:
                obj.append(instance.to_dictionary())
        json_obj = cls.to_json_string(obj)
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(json_obj)

    @staticmethod
    def from_json_string(json_string):
        """Converts from json to objects"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
