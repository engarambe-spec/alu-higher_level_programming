#!/usr/bin/python3
"""Module that defines a text_indentation function.

This module provides a single function, text_indentation, that prints
a text with extra newlines after each ., ? and : character.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each ., ? and : character.

    Args:
        text: the string to print

    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    stripped = text.strip()
    line = ""
    for char in stripped:
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
