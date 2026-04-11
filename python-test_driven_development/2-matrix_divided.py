#!/usr/bin/python3
"""This module provides a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix with all values divided by div."""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix) or
            not all(all(isinstance(x, (int, float)) for x in row)
                    for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(x / div, 2) for x in row] for row in matrix]
