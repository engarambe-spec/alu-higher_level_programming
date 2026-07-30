#!/usr/bin/python3
"""Module for printing a person's full name.

This module defines a single function, say_my_name, which prints a
greeting using a first and optional last name.
"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first_name> <last_name>'.

    Args:
        first_name: the first name, must be a string.
        last_name: the last name, must be a string (default "").

    Raises:
        TypeError: if first_name is not a string.
        TypeError: if last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
