#!/usr/bin/python3
import numpy as np

"""
This module Provides a function that multiplies two matrix
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrix using numpy module
    """
    return np.matmul(m_a, m_b)
