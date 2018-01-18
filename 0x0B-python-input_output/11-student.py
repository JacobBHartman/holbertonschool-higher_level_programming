#!/usr/bin/python3
"""
    this module contains a class called Student
"""


class Student:
    """
        a student, like the ones in school!
    """

    def __init__(self, first_name, last_name, age):
        """ a method that is magic and initializes a student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
            return(vars(self))
