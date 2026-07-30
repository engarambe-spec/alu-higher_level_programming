#!/usr/bin/python3
"""Module that defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square

        Args:
            size: the size of the square (width and height)
            x: the x coordinate of the square
            y: the y coordinate of the square
            id: the identity of the new instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square (updates both width and height)"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes via no-keyword or keyworded arguments

        Args:
            *args: new attribute values in order id, size, x, y
            **kwargs: new attribute values as key/value pairs
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
