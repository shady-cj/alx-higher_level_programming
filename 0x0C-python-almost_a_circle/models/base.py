#!/usr/bin/python3


"""
This module defines a base class
"""

import json
import csv
import turtle


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
        if type(dictionary) == dict and len(dictionary):
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)
            else:
                obj = cls(1)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        saving the list_objs into a csv file
        """

        filename = cls.__name__ + ".csv"
        new_listobjs = []
        for obj in list_objs:
            obj_info = []
            obj_dict = obj.to_dictionary()
            obj_info.append(obj_dict.get("id"))
            if obj_dict.get("size") is not None:
                obj_info.append(obj_dict.get("size"))
            else:
                obj_info.append(obj_dict.get("width"))
                obj_info.append(obj_dict.get("height"))
            obj_info.append(obj_dict.get("x"))
            obj_info.append(obj_dict.get("y"))

            new_listobjs.append(obj_info)

        with open(filename, "w") as f:
            writer = csv.writer(f)
            for row in new_listobjs:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads from csv file and convert to list of instance
        """

        filename = cls.__name__ + ".csv"
        list_objs = []
        try:
            with open(filename) as f:
                reader = csv.reader(f)

                for row in reader:
                    list_objs.append(row)
        except FileNotFoundError:
            return []
        new_list_objs = []
        for obj in list_objs:
            obj = list(map(int, obj))
            instance = cls(1, 1)
            instance.update(*obj)
            new_list_objs.append(instance)
        return new_list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        This method provides the utility to draw the shapes using
        turtle
        """
        import random
        t = turtle.Turtle()
        t.setposition(0, 0)
        colors = ["red", "blue", "green", "yellow", "orange"]
        spacing = 20
        max_width = 0
        for rect in list_rectangles:
            if rect.width > max_width:
                max_width = rect.width
            t.color(random.choice())

            t.begin_fill()
            t.penup()
            t.forward(rect.x)
            t.right(90)
            t.forward(rect.y)
            t.left(90)
            t.pendown()
            t.forward(rect.width)
            t.right(90)
            t.forward(rect.height)
            t.right(90)
            t.forward(rect.width)
            t.right(90)
            t.forward(rect.height)
            t.penup()
            t.right(180)
            t.forward(rect.height + spacing)
            t.left(90)
            t.pendown()
            t.end_fill()
        t.setposition(max_width + spacing, 0)
        for sq in list_squares:
            t.color(random.choice())

            t.begin_fill()
            t.penup()
            t.forward(sq.x)
            t.right(90)
            t.forward(sq.y)
            t.left(90)
            t.pendown()
            t.forward(sq.size)
            t.right(90)
            t.forward(sq.size)
            t.right(90)
            t.forward(sq.size)
            t.right(90)
            t.forward(sq.size)
            t.penup()
            t.right(180)
            t.forward(sq.size + spacing)
            t.left(90)
            t.pendown()
            t.end_fill()
        t.done()
