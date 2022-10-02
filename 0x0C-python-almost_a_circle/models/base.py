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

    @classmethod
    def create(cls, **dictionary):
        """
        It returns an instance of the corresponding class
        with attributes listed in dictionary
        """

        obj = cls(2, 4)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        This method loads and returns a list of instances
        previously stored in a file
        """

        filename = cls.__name__ + ".json"

        try:
            content = None
            with open(filename, "r") as f:
                content = f.read()
            obj_list = cls.from_json_string(content)
            list_of_instances = []
            for d in obj_list:
                instance = cls.create(**d)
                list_of_instances.append(instance)
            return list_of_instances
        except FileNotFoundError:
            return []
