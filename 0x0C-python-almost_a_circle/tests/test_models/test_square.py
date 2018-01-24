#!/usr/bin/python3


import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import sys

class TestRectangleClass(unittest.TestCase):

    # test initialization, getters and setters
    def test_init_and_getter(self):
        r1 = Rectangle(10, 11, 4, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 11)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_setters(self):
        r1= Rectangle(10, 11, 4, 5)
        r1.width = 20
        r1.height = 22
        r1.x = 6
        r1.y = 9
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 22)
        self.assertEqual(r1.x, 6)
        self.assertEqual(r1.y, 9)
    
    # test types of any attribute value
    def test_attribute_is_dict(self):
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle({'ky': "val"}, 4, 3, 2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_attribute_is_list(self):
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(["a", "small", "list"], 4, 3, 2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_attribute_is_zero(self):
        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(0, 5, 4, 3)
        self.assertEqual(str(err.exception), "width must be > 0")

    # test width
    def test_width_is_str(self):
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle("Bamboozle", 5, 4, 3)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_width_is_float(self):
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(55.555, 4, 3, 2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_width_is_negative(self):
        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(-1, 5, 4, 3)
        self.assertEqual(str(err.exception), "width must be > 0")

    # test height
    def test_height_is_not_int(self):
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, "uhsuhdude", 4, 3)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_height_is_zero(self):
        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(5, 0, 4, 3)
        self.assertEqual(str(err.exception), "height must be > 0")

    def test_height_is_negative(self):
        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(5, -1, 4, 3)
        self.assertEqual(str(err.exception), "height must be > 0")

    # test x
    def test_x_is_not_int(self):
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, "whatchuwantsucka", 3)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_x_is_negative(self):
        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(5, 4, -1, 3)
        self.assertEqual(str(err.exception), "x must be >= 0")

    # test y
    def test_y_is_not_int(self):
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, 3, "applesandorangelos")
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_y_is_negative(self):
        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(5, 4, 3, -1)
        self.assertEqual(str(err.exception), "y must be >= 0")

    # test area(), display(), __str__, toDictionary
    def test_area_return(self):
        r1 = Rectangle(5, 4, 3, 3)
        self.assertEqual(r1.area(), 20)

    def test_display_nnnn(self):
        r1 = Rectangle(3, 3, 3, 3)
        string = "\n\n\n   ###\n   ###\n   ###\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1.display()
        self.assertEqual(captured_output.getvalue(), string)
        sys.stdout = sys.__stdout__

    def test_dunder_str(self):
        r1 = Rectangle(11, 12, 13, 14, 98)
        expected = "[Rectangle] (98) 13/14 - 11/12\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(r1)
        self.assertEqual(captured_output.getvalue(), expected)
        sys.stdout = sys.__stdout__

    def test_to_dictionary(self):
        r1 = Rectangle(4, 5)
        expected1 = {'width': 4, 'height': 5, 'x': 0, 'y': 0, 'id': 12}
        self.assertEqual(Rectangle.to_dictionary(r1), expected1)

    # test args and kwargs
    def test_kwargs_args_doesnt_exist(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(y=11, height=11, width=11, x=11)
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 11)
        self.assertEqual(r1.x, 11)
        self.assertEqual(r1.y, 11)

    """ PYTHON ERROR
    def test_update_args_is_empty(self):
        r1 = Rectangle(1, 2, 3, 4)
        with self.assertRaises(SyntaxError) as err:
            r1.update(width=5, height=6, x=7, y=8, 9, 10, 11, 12)
        self.assertEqual(str(err.exception), "non-keyword arg after keyword arg")
    """

    def test_args_update_lotsa(self):
        r1 = Rectangle(5, 5, 5, 5, 107)
        r1.update(107, 4, 3, 2, 0, 1, 1, 1, 1, 1)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 0)

    def test_args_update_five(self):
        r1 = Rectangle(9, 8, 7, 6, 5)
        r1.update(11, 12, 13, 14, 15)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 13)
        self.assertEqual(r1.x, 14)
        self.assertEqual(r1.y, 15)
        self.assertEqual(r1.id, 11)

    def test_args_update_four(self):
        r1 = Rectangle(9, 8, 7, 6, 5)
        r1.update(11, 12, 13, 14)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 13)
        self.assertEqual(r1.x, 14)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 11)

    def test_args_update_three(self):
        r1 = Rectangle(9, 8, 7, 6, 5)
        r1.update(11, 12, 13)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 13)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 11)

    def test_args_update_two(self):
        r1 = Rectangle(9, 8, 7, 6, 5)
        r1.update(11, 12)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 11)

    def test_args_update_one(self):
        r1 = Rectangle(9, 8, 7, 6, 5)
        r1.update(11)
        self.assertEqual(r1.width, 9)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 11)

    # test kwargs
    def test_kwargs_five_and_arg(self):
        r1 = Rectangle(9, 8, 7, 6, 5)
        r1.update(15, id=55, width=66, height=77, x=88, y=99)
        self.assertEqual(r1.width, 66)
        self.assertEqual(r1.height, 77)
        self.assertEqual(r1.x, 88)
        self.assertEqual(r1.y, 99)
        self.assertEqual(r1.id, 55)

    def test_kwargs_four_and_arg(self):
        r1 = Rectangle(9, 8, 7, 6, 5)
        r1.update(15, id=55, width=66, height=77, x=88)
        self.assertEqual(r1.width, 66)
        self.assertEqual(r1.height, 77)
        self.assertEqual(r1.x, 88)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 55)

    def test_kwargs_three_and_arg(self):
        r1 = Rectangle(9, 8, 7, 6, 5)
        r1.update(15, id=55, width=66, height=77)
        self.assertEqual(r1.width, 66)
        self.assertEqual(r1.height, 77)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 55)

    def test_kwargs_four_and_arg(self):
        r1 = Rectangle(9, 8, 7, 6, 5)
        r1.update(15, id=55, width=66)
        self.assertEqual(r1.width, 66)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 55)

    def test_kwargs_four_and_arg(self):
        r1 = Rectangle(9, 8, 7, 6, 5)
        r1.update(15, id=55)
        self.assertEqual(r1.width, 9)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 55)

    def test_arg_five_kwarg_one(self):
        r1 = Rectangle(5, 6, 7, 8, 9)
        r1.update(10, 11, 12, 13, 14, id=20)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 12)
        self.assertEqual(r1.x, 13)
        self.assertEqual(r1.y, 14)

    def test_arg_five_kwarg_two(self):
        r1 = Rectangle(5, 6, 7, 8, 9)
        r1.update(10, 11, 12, 13, 14, id=20, width=30)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 12)
        self.assertEqual(r1.x, 13)
        self.assertEqual(r1.y, 14)

    def test_arg_five_kwarg_three(self):
        r1 = Rectangle(5, 6, 7, 8, 9)
        r1.update(10, 11, 12, 13, 14, id=20, width=30, height=40)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 12)
        self.assertEqual(r1.x, 13)
        self.assertEqual(r1.y, 14)

    def test_arg_five_kwarg_four(self):
        r1 = Rectangle(5, 6, 7, 8, 9)
        r1.update(10, 11, 12, 13, 14, id=20, width=30, height=40, x=50)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 12)
        self.assertEqual(r1.x, 13)
        self.assertEqual(r1.y, 14)

    def test_arg_five_kwarg_five(self):
        r1 = Rectangle(5, 6, 7, 8, 9)
        r1.update(10, 11, 12, 13, 14, id=20, width=30, height=40, x=50, y=60)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 12)
        self.assertEqual(r1.x, 13)
        self.assertEqual(r1.y, 14)

