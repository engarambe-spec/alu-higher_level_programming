#!/usr/bin/python3
"""Module that defines a class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description of a simple data structure object

    Args:
        obj: an instance of a class with serializable attributes

    Returns:
        A dictionary representation of the object suitable for JSON
    """
    return obj.__dict__
