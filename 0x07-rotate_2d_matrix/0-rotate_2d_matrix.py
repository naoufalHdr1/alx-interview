#!/usr/bin/env python3
"""
This module contains a function to rotate a 2D matrix 90 degrees
clockwise in-place.
"""
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """ Rotates a 2D matrix 90 degrees clockwise in-place.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()