#!/usr/bin/python3
"""Module for dividing all elements of a matrix by a divisor.

This module defines a single function, matrix_divided, which returns
a new matrix with every element divided by a given number, rounded to
2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix: a list of lists of integers or floats. Every row must
            be the same length.
        div: the number (integer or float) to divide each element by.

    Returns:
        A new matrix (list of lists of floats) with each element of
        matrix divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of ints/floats.
        TypeError: if the rows of matrix aren't all the same size.
        TypeError: if div is not an integer or a float.
        ZeroDivisionError: if div is equal to 0.
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_matrix)
        for value in row:
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(err_matrix)
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(value / div, 2) for value in row] for row in matrix]
