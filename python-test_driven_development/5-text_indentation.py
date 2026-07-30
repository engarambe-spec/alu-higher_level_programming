#!/usr/bin/python3
"""Module for printing text with extra indentation after punctuation.

This module defines a single function, text_indentation, which prints
a block of text with two new lines inserted after each '.', '?', and
':' character.
"""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: the string to print.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print("")
            line = ""
    if line.strip():
        print(line.strip(), end="")
