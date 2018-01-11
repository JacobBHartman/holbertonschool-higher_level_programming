#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_none(self):
        """Testing when None value is passed"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_correct(self):
        """Testing correct output"""
        self.assertEqual(max_integer([1, 6, 100, 4, 0, -1, 10]), 100)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)
        self.assertEqual(max_integer([5, 1, 2, 3, 4]), 5)
        self.assertEqual(max_integer([5]), 5)

    def test_list_empty(self):
        """Testing if list is empty"""
        self.assertIsNone(max_integer([]))

    def test_no_parameter(self):
        """Testing when theres not parameter"""
        self.assertIsNone(max_integer())

    def test_all_same(self):
        """Testing when all values are equal"""
        self.assertEqual(max_integer([1, 1, 1, 1, 1]), 1)

    def test_non_ints(self):
        """Test when list contains non-ints"""
        with self.assertRaises(TypeError):
            max_integer([1, "hello", 2.3, 45])

    def test_only_negatives(self):
        """Test if theres only negatives"""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
