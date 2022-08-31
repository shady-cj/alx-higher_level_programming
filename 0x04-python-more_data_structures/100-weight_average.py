#!/usr/bin/python3


def weight_average(my_list=[]):
    sum = 0
    mul_sum = 0
    for score, weight in my_list:
        mul_sum += score * weight
        sum += weight
    return mul_sum / sum
