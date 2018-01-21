#!/usr/bin/python3
"""
    this module contains a class called Base which will act as the 'base'
    of all other classes in this project. the goal of it is to manage 'id'
    attribute in all future classes and to ensure that code (and a bug)
    is not duplicated.
"""


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
