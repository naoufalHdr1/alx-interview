#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Parameters:
    n (int): The number of rows to generate.

    Returns:
    triangle: A list of lists representing Pascal's Triangle.
    """
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle
