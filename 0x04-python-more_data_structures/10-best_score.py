#!/usr/bin/python3


def best_score(a_dictionary):
    highest_key = None
    value = None
    if a_dictionary is None:
        return highest_key
    for k, v in a_dictionary.items():
        if value is None or v > value:
            value = v
            highest_key = k
    return highest_key
