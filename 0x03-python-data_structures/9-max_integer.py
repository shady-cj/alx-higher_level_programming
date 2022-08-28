#!/usr/bin/python3

def max_integer(my_list=[]):
    largest = None

    for i in my_list:
        if largest is None:
            largest = i
        else:
            if i > largest:
                largest = i
    return largest
