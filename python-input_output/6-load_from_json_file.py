#!/usr/bin/python3
"""Module that defines a load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file

    Args:
        filename: the name of the file to read from

    Returns:
        The Python data structure represented in the file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
