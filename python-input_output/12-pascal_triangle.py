#!/usr/bin/python3
"""Module that creates Pascal's Triangle"""


def pascal_triangle(n):
    """Creates a list of lists representing Pascal's Triangle

    Args:
        n (int): Number of rows to generate

    Returns:
        list: List of lists of integers representing Pascal's Triangle
        Returns empty list if n <= 0
    """
    if n <= 0:
        return []

    # Initialize triangle with first row
    triangle = [[1]]

    # Generate remaining rows
    for i in range(n - 1):
        # Get the previous row
        prev_row = triangle[-1]
        # Start new row with 1
        new_row = [1]

        # Calculate middle numbers
        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j + 1])

        # End new row with 1
        new_row.append(1)

        # Add the new row to triangle
        triangle.append(new_row)

    return triangle
