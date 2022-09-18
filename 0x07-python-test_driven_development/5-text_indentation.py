#!/usr/bin/python3
"""
A module containing a function that prints a text with 2 new lines
after each of these characters: ., ? and :

    - Prototype: def text_indentation(text):
    - text must be a string, otherwise raise a TypeError exception
        with the message text must be a string
    - There should be no space at the beginning or at
        the end of each printed line
    - You are not allowed to import any module
"""

def text_indentation(text):
    """
    The function accepts a string as an argument parses/validate it
    and prints the string and new line at every . : or ?
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    line_text = ""

    for char in text:
        line_text += char
        if char in ('.', ':', '?'):
            line_text = line_text.strip()
            print(line_text)
            line_text = ""
            print()
    print(line_text.strip(), end="")
