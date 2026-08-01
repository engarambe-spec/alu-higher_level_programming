#!/usr/bin/python3
"""Module that defines an add_integer function.

This module provides a single function, add_integer, that adds two
numbers together after casting them to integers.
"""


def add_integer(a, b=98):
    """Adds two integers or floats, casting floats to integers first.

    Args:
        a: the first number (int or float)
        b: the second number (int or float), defaults to 98

    Returns:
        The integer sum of a and b

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
