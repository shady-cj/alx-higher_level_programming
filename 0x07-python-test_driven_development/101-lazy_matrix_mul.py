#!/usr/bin/python3
"""
This module Provides a function that multiplies two matrix
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrix using numpy module
    """
    return np.matmul(m_a, m_b)
