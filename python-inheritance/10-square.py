
#!/usr/bin/python3

"""Module that defines a class Square, inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle





class Square(Rectangle):

    """Represents a square."""



    def __init__(self, size):

        """Initializes a new Square.



        Args:

            size: the size of the square.



        Raises:

            TypeError: if size is not an integer.

            ValueError: if size is <= 0.

        """

        self.integer_validator("size", size)

        super().__init__(size, size)

