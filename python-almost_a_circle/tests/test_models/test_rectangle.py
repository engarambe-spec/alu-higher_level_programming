#!/usr/bin/python3
"""Unit tests for the Rectangle class"""
import unittest
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """Tests for Rectangle instantiation"""

    def setUp(self):
        """Resets the Base nb_objects counter before each test"""
        Base._Base__nb_objects = 0

    def test_width_height(self):
        """Tests basic instantiation with width and height only"""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_full_args(self):
        """Tests instantiation with all arguments"""
        r = Rectangle(10, 2, 1, 3, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 12)

    def test_id_autoincrement(self):
        """Tests id auto-increments when not given"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_is_base_instance(self):
        """Tests that a Rectangle is also a Base instance"""
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Base)

    def test_module_docstring(self):
        """Tests that the module has documentation"""
        self.assertTrue(len(__import__(
            "models.rectangle", fromlist=["rectangle"]).__doc__) > 0)

    def test_class_docstring(self):
        """Tests that the class has documentation"""
        self.assertTrue(len(Rectangle.__doc__) > 0)


class TestRectangleValidation(unittest.TestCase):
    """Tests for Rectangle attribute validation"""

    def test_width_not_int(self):
        """Tests width as a non-integer raises TypeError"""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(10, "2")
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_width_zero(self):
        """Tests width of 0 raises ValueError"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(0, 2)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_width_negative(self):
        """Tests negative width raises ValueError"""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as ctx:
            r.width = -10
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_height_not_int(self):
        """Tests height as a non-integer raises TypeError"""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(2, "10")
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_height_negative(self):
        """Tests negative height raises ValueError"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(10, -2)
        self.assertEqual(str(ctx.exception), "height must be > 0")

    def test_x_not_int(self):
        """Tests x as a non-integer raises TypeError"""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as ctx:
            r.x = {}
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_x_negative(self):
        """Tests negative x raises ValueError"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(10, 2, -1, 0)
        self.assertEqual(str(ctx.exception), "x must be >= 0")

    def test_y_negative(self):
        """Tests negative y raises ValueError"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(ctx.exception), "y must be >= 0")

    def test_y_not_int(self):
        """Tests y as a non-integer raises TypeError"""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as ctx:
            r.y = "1"
        self.assertEqual(str(ctx.exception), "y must be an integer")


class TestRectangleArea(unittest.TestCase):
    """Tests for Rectangle.area"""

    def test_area_basic(self):
        """Tests the area of a simple rectangle"""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_after_update(self):
        """Tests that area reflects updated dimensions"""
        r = Rectangle(3, 2)
        r.width = 10
        self.assertEqual(r.area(), 20)


class TestRectangleDisplay(unittest.TestCase):
    """Tests for Rectangle.display"""

    def test_display_no_offset(self):
        """Tests display without x/y offset"""
        r = Rectangle(2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "##\n##\n")

    def test_display_with_offset(self):
        """Tests display with x/y offset"""
        r = Rectangle(2, 2, 1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "\n ##\n ##\n")


class TestRectangleStr(unittest.TestCase):
    """Tests for Rectangle.__str__"""

    def test_str(self):
        """Tests the string representation of a Rectangle"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


class TestRectangleUpdate(unittest.TestCase):
    """Tests for Rectangle.update"""

    def test_update_args(self):
        """Tests update with no-keyword arguments"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Tests update with keyworded arguments"""
        r = Rectangle(10, 10, 10, 10)
        r.update(x=1, height=2, y=3, width=4, id=1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/3 - 4/2")

    def test_update_args_skips_kwargs(self):
        """Tests that kwargs are ignored when args is not empty"""
        r = Rectangle(10, 10)
        r.update(5, width=99)
        self.assertEqual(r.id, 5)
        self.assertNotEqual(r.width, 99)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for Rectangle.to_dictionary"""

    def test_to_dictionary(self):
        """Tests the dictionary representation of a Rectangle"""
        r = Rectangle(10, 2, 1, 9, 1)
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_to_dictionary_round_trip(self):
        """Tests that a Rectangle can be rebuilt from its dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
