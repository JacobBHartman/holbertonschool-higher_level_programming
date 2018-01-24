#!/usr/bin/python3
"""
    this module contains a class called Base which will act as the 'base'
    of all other classes in this project. the goal of it is to manage 'id'
    attribute in all future classes and to ensure that code (and a bug)
    is not duplicated.
"""


import json


class Base:
    """
        this class acts as the 'base' of all other classes in this project.
        this will help manage the 'id' attribute in all future classes and
        to ensure that code and bugs are not duplicated

        Attributes:
            nb_objects: number of objects assigned an id when id is not given
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            this method is a magic one and initializes attribute for an
            instance of class 'Base'

            Args:
                id: unique id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            return the JSON string representation of the dictionary
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON string representation of the object to a file
        """
        list_dicts = []
        filename = "{}.json".format(cls.__name__)

        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(cls.to_dictionary(obj))
        json_string = Base.to_json_string(list_dicts)
        with open(filename, mode='w+', encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
            return the list of the JSON string representation
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            return an instance with all attributes already set
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
            return a list of instances
        """
        filename = cls.__name__ + ".json"
        new_list = []

        if filename is None:
            return []

        # get a string from json file
        with open(filename, mode='r', encoding='utf-8') as json_file:
            json_string = json_file.read()

        list_of_dicts = cls.from_json_string(json_string)

        for dct in list_of_dicts:
            new_list.append(cls.create(**dct))

        return new_list
