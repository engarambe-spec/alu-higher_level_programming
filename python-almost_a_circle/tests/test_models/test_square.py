#!/usr/bin/python3
"""Unit tests for the Square class"""
import unittest
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInit(unittest.TestCase):
    """Tests for Square instantiation"""

    def setUp(self):
        """Resets the Base nb_objects counter before each test"""
        Base._Base__nb_objects = 0

    def test_size_only(self):
        """Tests instantiation with size only"""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_full_args(self):
        """Tests instantiation with all arguments"""
        s = Square(5, 1, 2, 10)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 10)

    def test_is_rectangle_instance(self):
        """Tests that a Square is also a Rectangle instance"""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_is_base_instance(self):
        """Tests that a Square is also a Base instance"""
        s = Square(5)
        self.assertIsInstance(s, Base)

    def test_no_new_attributes(self):
        """Tests that Square does not create new instance attributes"""
        s = Square(5)
        self.assertEqual(
            set(s.__dict__.keys()),
            {"_Rectangle__width", "_Rectangle__height",
             "_Rectangle__x", "_Rectangle__y", "id"})

    def test_validation_inherited(self):
        """Tests that Square inherits Rectangle's validation"""
        with self.assertRaises(TypeError) as ctx:
            Square("5")
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_module_docstring(self):
        """Tests that the module has documentation"""
        self.assertTrue(len(__import__(
            "models.square", fromlist=["square"]).__doc__) > 0)

    def test_class_docstring(self):
        """Tests that the class has documentation"""
        self.assertTrue(len(Square.__doc__) > 0)


class TestSquareStr(unittest.TestCase):
    """Tests for Square.__str__"""

    def test_str(self):
        """Tests the string representation of a Square"""
        s = Square(3, 1, 3, 5)
        self.assertEqual(str(s), "[Square] (5) 1/3 - 3")


class TestSquareArea(unittest.TestCase):
    """Tests for Square.area (inherited from Rectangle)"""

    def test_area(self):
        """Tests the area of a Square"""
        s = Square(5)
        self.assertEqual(s.area(), 25)


class TestSquareDisplay(unittest.TestCase):
    """Tests for Square.display (inherited from Rectangle)"""

    def test_display(self):
        """Tests display of a Square"""
        s = Square(2)
        f = io.StringIO()
        with redirect_stdout(f):
            s.display()
        self.assertEqual(f.getvalue(), "##\n##\n")


class TestSquareSize(unittest.TestCase):
    """Tests for the Square size property"""

    def test_size_getter(self):
        """Tests that size getter returns width"""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Tests that setting size updates both width and height"""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.size, 10)

    def test_size_setter_validation(self):
        """Tests that the size setter validates like width"""
        s = Square(5)
        with self.assertRaises(TypeError) as ctx:
            s.size = "9"
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_size_setter_negative(self):
        """Tests that a negative size raises ValueError"""
        s = Square(5)
        with self.assertRaises(ValueError) as ctx:
            s.size = -1
        self.assertEqual(str(ctx.exception), "width must be > 0")


class TestSquareUpdate(unittest.TestCase):
    """Tests for Square.update"""

    def test_update_args(self):
        """Tests update with no-keyword arguments"""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Tests update with keyworded arguments"""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_update_args_skips_kwargs(self):
        """Tests that kwargs are ignored when args is not empty"""
        s = Square(5)
        s.update(10, size=99)
        self.assertEqual(s.id, 10)
        self.assertNotEqual(s.size, 99)


class TestSquareToDictionary(unittest.TestCase):
    """Tests for Square.to_dictionary"""

    def test_to_dictionary(self):
        """Tests the dictionary representation of a Square"""
        s = Square(10, 2, 1, 1)
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_to_dictionary_round_trip(self):
        """Tests that a Square can be rebuilt from its dictionary"""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
