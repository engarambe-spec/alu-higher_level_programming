#!/usr/bin/python3
"""Module that defines an inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that is a subclass,
    directly or indirectly, of the specified class

    Args:
        obj: the object to check
        a_class: the class to compare against

    Returns:
        True if obj is an instance of a subclass of a_class, else False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
