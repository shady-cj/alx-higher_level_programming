#!/usr/bin/python3
"""
Contains a function thats finds a peak in a
list of unsorted integers
"""

def find_peak(list_of_integers):
    """
    Implementing the find_peak function
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    mid = len(list_of_integers) // 2
    left = find_peak(list_of_integers[0:mid])
    right = find_peak(list_of_integers[mid:])
    if right is not None and left is not None:
        if right >= left:
            return right
        else:
            return left
    else:
        return right or left
