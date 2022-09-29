#!/usr/bin/python3

"""
Implement search and append in this module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function appends and replace
    """
    t = ""
    with open(filename, "r") as f:
        for line in f:
            if line.find(search_string) != -1:
                line += new_string
            t += line
    with open(filename, "w") as f:
        f.write(t)
