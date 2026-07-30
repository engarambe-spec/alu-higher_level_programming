#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """Tests a list already sorted in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Tests a list that is not sorted."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_start(self):
        """Tests a list where the max value is the first element."""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        """Tests a list where the max value is the last element."""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_empty_list(self):
        """Tests that an empty list returns None."""
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        """Tests calling the function with no argument at all."""
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        """Tests a list containing a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Tests a list of only negative numbers."""
        self.assertEqual(max_integer([-1, -5, -2]), -1)

    def test_mixed_positive_and_negative(self):
        """Tests a list mixing positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_all_same_values(self):
        """Tests a list where every value is identical."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        """Tests a list of floating point numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_duplicate_max_values(self):
        """Tests a list where the max value appears more than once."""
        self.assertEqual(max_integer([3, 9, 9, 2]), 9)


if __name__ == "__main__":
    unittest.main()
