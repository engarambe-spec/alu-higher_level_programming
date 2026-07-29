#!/usr/bin/python3
"""Module that defines a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initializes a new Square

        Args:
            size: the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
