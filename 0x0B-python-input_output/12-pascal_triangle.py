#!/usr/bin/python3


"""
A module that returns pascal triangle
"""


def pascal_triangle(n):
    """
    The function returns out pascal triangle
    """
    triangle = []
    if n <= 0:
        return []

    for i in range(n):
        prev = i - 1
        row = []
        if prev < 0:
            row.append(1)
        else:
            j = 0
            row.append(1)
            width = len(triangle[prev])
            while j + 1 < width:
                present = triangle[prev][j]
                nextt = triangle[prev][j+1]
                row.append(present + nextt)
                j += 1
            row.append(1)
        triangle.append(row)
    return triangle
