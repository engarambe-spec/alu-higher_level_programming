#!/usr/bin/python3
"""Module that defines an append_write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)

    Args:
        filename: the name of the file to append to
        text: the string to append

    Returns:
        The number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
