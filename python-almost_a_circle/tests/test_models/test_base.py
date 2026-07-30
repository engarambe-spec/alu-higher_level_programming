#!/usr/bin/python3
"""Unit tests for the Base class"""
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def setUp(self):
        """Resets the Base nb_objects counter before each test"""
        Base._Base__nb_objects = 0

    def test_id_default(self):
        """Tests that id auto-increments when not given"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_given(self):
        """Tests that a given id is used as-is"""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_given_does_not_increment_counter(self):
        """Tests that giving an explicit id does not touch the counter"""
        Base(12)
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_module_docstring(self):
        """Tests that the module has documentation"""
        self.assertTrue(len(__import__("models.base",
                                        fromlist=["base"]).__doc__) > 0)

    def test_class_docstring(self):
        """Tests that the class has documentation"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_init_docstring(self):
        """Tests that __init__ has documentation"""
        self.assertTrue(len(Base.__init__.__doc__) > 0)


class TestBaseToJSONString(unittest.TestCase):
    """Tests for Base.to_json_string"""

    def test_none(self):
        """Tests None input returns '[]'"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """Tests empty list input returns '[]'"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        """Tests a normal list of dictionaries"""
        list_dicts = [{"id": 1}, {"id": 2}]
        result = Base.to_json_string(list_dicts)
        self.assertEqual(json.loads(result), list_dicts)

    def test_return_type(self):
        """Tests that the return value is a string"""
        self.assertIsInstance(Base.to_json_string([{"id": 1}]), str)


class TestBaseFromJSONString(unittest.TestCase):
    """Tests for Base.from_json_string"""

    def test_none(self):
        """Tests None input returns an empty list"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """Tests empty string input returns an empty list"""
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json(self):
        """Tests a valid JSON string round-trips correctly"""
        list_dicts = [{"id": 1}, {"id": 2}]
        json_string = json.dumps(list_dicts)
        self.assertEqual(Base.from_json_string(json_string), list_dicts)

    def test_return_type(self):
        """Tests that the return value is a list"""
        self.assertIsInstance(Base.from_json_string("[]"), list)


class TestBaseSaveToFile(unittest.TestCase):
    """Tests for Base.save_to_file"""

    def setUp(self):
        """Removes any leftover files before each test"""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def tearDown(self):
        """Removes any files created during the tests"""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_rectangles(self):
        """Tests saving a list of Rectangle instances to file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json") as f:
            content = json.loads(f.read())
        self.assertEqual(len(content), 2)

    def test_save_none(self):
        """Tests saving None writes an empty list to file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_overwrites_file(self):
        """Tests that saving overwrites any existing file content"""
        r1 = Rectangle(1, 1)
        Rectangle.save_to_file([r1])
        r2 = Rectangle(2, 2)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json") as f:
            content = json.loads(f.read())
        self.assertEqual(len(content), 1)


class TestBaseCreate(unittest.TestCase):
    """Tests for Base.create"""

    def test_create_rectangle(self):
        """Tests creating a Rectangle from a dictionary"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Tests creating a Square from a dictionary"""
        s1 = Square(5, 1, 2, 10)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Tests for Base.load_from_file"""

    def setUp(self):
        """Removes any leftover files before each test"""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def tearDown(self):
        """Removes any files created during the tests"""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_load_no_file(self):
        """Tests loading returns an empty list when no file exists"""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_rectangles(self):
        """Tests loading a list of Rectangle instances round-trips"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertEqual(str(loaded[1]), str(r2))

    def test_load_squares(self):
        """Tests loading a list of Square instances round-trips"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(s1))
        self.assertEqual(str(loaded[1]), str(s2))


if __name__ == "__main__":
    unittest.main()
