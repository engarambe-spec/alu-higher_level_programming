#!/usr/bin/python3
"""Module that defines a to_json_string function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object

    Args:
        my_obj: the object to serialize

    Returns:
        A string containing the JSON representation of my_obj
    """
    return json.dumps(my_obj)
