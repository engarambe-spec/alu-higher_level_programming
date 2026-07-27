#!/usr/bin/python3
"""Module that defines an is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of, or inherits from, a_class.

    Args:
        obj: the object to check.
        a_class: the class to check against.

    Returns:
        True if obj is an instance of a_class or of a class that
        inherited from a_class, otherwise False.
    """
    return isinstance(obj, a_class)
