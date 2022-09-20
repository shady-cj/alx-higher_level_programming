#!/usr/bin/python3


"""
A module that provides a function that multiply two matrix.
"""


def matrix_mul(m_a, m_b):
    """
    The function multiplies 2 matrix (list of lists)
    and raises exception if there is any form of
    impossibilities in multiplying
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    result = []
    len_a = len(m_a[0]) if len(m_a) and type(m_a[0]) == list else 0
    len_b = len(m_b[0]) if len(m_b) and type(m_b[0]) == list else 0

    for ma in m_a:
        if type(ma) != list:
            raise TypeError("m_a must be a list of lists")
        if len(ma) != len_a:
            raise TypeError("each row of m_a must be of the same size")
        for a in ma:
            if type(a) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for mb in m_b:
        if type(mb) != list:
            raise TypeError("m_b must be a list of lists")
        if len(mb) != len_b:
            raise TypeError("each row of m_b must be of the same size")
        for b in mb:
            if type(b) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for idx in range(len(m_a)):
        new_arr = []
        row = m_a[idx]
        for i in range(len_b):
            points = 0
            for j in range(len(row)):
                try:
                    points += row[j] * m_b[j][i]
                except IndexError:
                    raise ValueError("m_a and m_b \
can't be multiplied") from None
            new_arr.append(points)
        result.append(new_arr)
    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return result
