#!/usr/bin/python3

"""
Defining the MyList class
"""


class MyList(list):
    """
    inheriting from list class and also defining the print_sorted method
    """
   
    def print_sorted(self):
        sorted_list = list(self)
        sorted_list.sort()
        print(sorted_list)
