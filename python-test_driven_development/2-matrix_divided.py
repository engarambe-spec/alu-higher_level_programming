#!/usr/bin/python3
"""Module that defines a matrix_divided function.

This module provides a single function, matrix_divided, that returns
a new matrix with every element divided by a given divisor.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix: a list of lists of integers or floats
        div: the number to divide every element by

    Returns:
        A new matrix (list of lists) with every element divided by div

    Raises:
        TypeError: if matrix is not a list of lists of ints/floats
        TypeError: if the rows of matrix are not all the same size
        TypeError: if div is not an integer or a float
        ZeroDivisionError: if div is equal to 0
    """
    matrix_error = "matrix must be a matrix (list of lists) of " \
        "integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(matrix_error)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(matrix_error)
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(matrix_error)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same "
                             "size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
