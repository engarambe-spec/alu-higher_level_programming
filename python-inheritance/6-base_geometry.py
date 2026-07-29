#!/usr/bin/python3
"""Module that defines a class BaseGeometry"""


class BaseGeometry:
    """Represents a base geometry object"""

    def area(self):
        """Raises an exception since area is not implemented here"""
        raise Exception("area() is not implemented")
