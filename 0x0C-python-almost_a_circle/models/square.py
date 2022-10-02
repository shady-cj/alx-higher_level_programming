#!/usr/bin/python3

"""
This modules a Square with all the necessary functionalities
and inherits from the Rectangle class
"""

from .rectangle import Rectangle



class Square(Rectangle):
    """
    Defining a Square class that inherits from
    Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        The constructor... inheriting from the parent class
        and also adding new attributes
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def get_size(self):
        """
        defining getter on size attribute
        """
        return self.width

    def set_size(self, s):
        """
        defining setter on size
        """
        self.width = s
        self.height = s

    size = property(get_size, set_size)


    def update(self, *args, **kwargs):
        """
        Allowing updates on the class attributes
        """
        i = 0
        u_dict = {
                "id": 0,
                "size": 0,
                "x": 0,
                "y": 0
                }
        while i < len(args):
            if i == 0:
                self.id = args[i]
                u_dict["id"] += 1
            elif i == 1:
                self.size = args[i]
                u_dict["size"] += 1
            elif i == 2:
                self.x = args[i]
                u_dict["x"] += 1
            elif i == 3:
                self.y = args[i]
                u_dict["y"] += 1
            i += 1
        for k, v in kwargs.items():
            if u_dict[k] == 0:
                setattr(self, k, v)

    def to_dictionary(self):
        """
        Converting the square instance to
        dictionary
        """
        d = super().to_dictionary()
        d["size"] = self.size
        d.pop("width")
        d.pop("height")
        return d
