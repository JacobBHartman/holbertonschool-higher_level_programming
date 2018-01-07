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

    def test_not_list(self):
        """Testing if theres a list"""
        with self.assertRaises(TypeError):
            max_integer("fasfsafs")

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
        with self.assertRaise(TypeError):
            max_integer([1, "hello", 2.3, 45])

    def test_float(self):
        """Test if theres floats"""
        with self.assertRaise(TypeError):
            max_integer([4.0, 3, 2, 1])

    def test_only_negatives(self):
        """Test if theres only negatives"""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
