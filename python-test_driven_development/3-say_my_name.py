#!/usr/bin/python3
"""Module that defines a say_my_name function.

This module provides a single function, say_my_name, that prints a
formatted greeting using a first and last name.
"""


def say_my_name(first_name, last_name=""):
    """Prints "My name is <first name> <last name>".

    Args:
        first_name: the first name to print
        last_name: the last name to print, defaults to an empty string

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
