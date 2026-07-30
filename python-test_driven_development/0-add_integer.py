#!/usr/bin/python3
"""Module for adding two integers.

This module defines a single function, add_integer, which adds two
numbers together after validating and casting them to integers.
"""


def add_integer(a, b=98):
    """Adds two integers or floats together, casting floats to int.

    Args:
        a: the first number, an integer or a float.
        b: the second number, an integer or a float (default 98).

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: if a is not an integer or float.
        TypeError: if b is not an integer or float.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
