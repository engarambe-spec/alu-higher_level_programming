#!/usr/bin/python3
"""Module that defines an is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class

    Args:
        obj: the object to check
        a_class: the class to compare against

    Returns:
        True if obj is exactly an instance of a_class, otherwise False
    """
    return type(obj) == a_class
