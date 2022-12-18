#!/usr/bin/python3
"""
Contains a function thats finds a peak in a
list of unsorted integers
"""


def find_peak(list_of_integers, lo=None, hi=None):
    """
    Implementing the find_peak function
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if lo is None and hi is None:
        lo = 0
        hi = len(list_of_integers) - 1
    mid = (lo + hi) // 2
    left = mid - 1
    right = mid + 1
    if left < 0 and list_of_integers[mid] >= list_of_integers[right]:
        return list_of_integers[mid]
    elif right >= len(list_of_integers) and\
            list_of_integers[mid] >= list_of_integers[left]:
        return list_of_integers[mid]
    elif list_of_integers[mid] >= list_of_integers[left] and\
            list_of_integers[mid] >= list_of_integers[right]:
        return list_of_integers[mid]
    if lo == hi:
        return None

    searchLeft = find_peak(list_of_integers, lo, mid)
    searchRight = find_peak(list_of_integers, mid + 1, hi)
    if searchLeft is None:
        return searchRight
    return searchLeft
