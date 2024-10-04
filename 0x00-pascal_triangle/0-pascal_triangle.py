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
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        previous_row = triangle[i - 1]
        new_row = [1]  # Start the row with 1

        # Create new elements for the current row by summing adjacent elements
        for j in range(1, len(previous_row)):
            new_row.append(previous_row[j - 1] + previous_row[j])

        new_row.append(1)  # End the row with 1
        triangle.append(new_row)

    return triangle
