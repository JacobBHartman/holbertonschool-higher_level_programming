#!/usr/bin/python3


import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    #task 0
    def test_base_obj_type(self):
        base_obj_ex = Base()
        self.assertEqual(type(base_obj_ex), type(Base()))

    def test_base_obj_id_type(self):
        base_obj_ex = Base()
        self.assertEqual(type(base_obj_ex.id), int)

    def test_base_obj_id(self):
        base_obj_1 = Base()
        base_obj_u = Base(234)
        base_obj_2 = Base()
        self.assertEqual(base_obj_1.id, 1)
        self.assertEqual(base_obj_u.id, 234)
        self.assertEqual(base_obj_2.id, 2)

    #task 15
    def test_if_toJsonString_returns_string(self):
        list_dict = [{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}]
        self.assertEqual(type(list_dict[0]), dict)
        self.assertEqual(type(list_dict), list)
        desired_string = Base.to_json_string(list_dict)
        self.assertEqual(type(desired_string), str)

    def test_if_toJsonString_returns_empty_list_string(self):
        list_dict = []
        self.assertEqual("[]", Base.to_json_string(list_dict))

    # task 16
    def test_saveToFile_if_list_objs_is_none(self):
        list_objs = []
        self.assertEqual(Base.save_to_file(list_objs), None)

    # task 17
    def test_if_fromJsonString_returns_normal(self):
        """ same as task 17 example, except replace Rectangle object with
        base """
        list_input = [{'id': 89}, {'id': 102}, {'id': 237}]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_output, [{'id': 89}, {'id': 102}, {'id': 237}])

    def test_if_fromJsonString_returns_empty(self):
        self.assertEqual(Base.from_json_string(None), [])
