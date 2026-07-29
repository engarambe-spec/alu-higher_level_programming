#!/usr/bin/python3
"""Module that defines an is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of the specified class,
    or an instance of a subclass of it

    Args:
        obj: the object to check
        a_class: the class to compare against

    Returns:
        True if obj is an instance of a_class or a subclass, otherwise False
    """
    return isinstance(obj, a_class)
