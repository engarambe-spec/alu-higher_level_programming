#!/usr/bin/python3
"""Module that defines a print_square function.

This module provides a single function, print_square, that prints a
square of a given size using the character #.
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size: the length of each side of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
