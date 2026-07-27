#!/usr/bin/python3
"""Module that defines an inherits_from function."""


def inherits_from(obj, a_class):
    """Checks if obj's class inherited (directly or indirectly) from a_class.

    Args:
        obj: the object to check.
        a_class: the class to check against.

    Returns:
        True if obj is an instance of a class that inherited from
        a_class, but is not a_class itself, otherwise False.
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
