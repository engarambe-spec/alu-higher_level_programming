#!/usr/bin/python3
"""Module that defines a write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)

    Args:
        filename: the name of the file to write to
        text: the string to write

    Returns:
        The number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
