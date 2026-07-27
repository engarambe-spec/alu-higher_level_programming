#!/usr/bin/python3
"""Module that defines a class BaseGeometry with an area method."""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Raises an Exception, since area() is not implemented here."""
        raise Exception("area() is not implemented")
