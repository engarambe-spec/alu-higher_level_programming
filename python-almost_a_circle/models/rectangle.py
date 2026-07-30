#!/usr/bin/python3
"""Module that defines the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
            x: the x coordinate of the rectangle
            y: the y coordinate of the rectangle
            id: the identity of the new instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x coordinate of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y coordinate of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle instance with the character #,
        taking x and y into account
        """
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns the string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates attributes via no-keyword or keyworded arguments

        Args:
            *args: new attribute values in order id, width, height, x, y
            **kwargs: new attribute values as key/value pairs
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
