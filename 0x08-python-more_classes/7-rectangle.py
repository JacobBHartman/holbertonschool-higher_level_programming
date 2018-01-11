#!/usr/bin/python3
"""this module contains a class which defines a rectangle"""


class Rectangle:
    """this class defines a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialization for a Rectangle

        Args:
            width (int): width of a Rectangle
            height (int): height of a Rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """int: gets the width of a Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: gets the height of a Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of a Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """makes the object readable and generates output for the user"""
        if self.__height == 0 or self.__width == 0:
            return ""
        pic = ""
        for i in range(self.__height):
            pic += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                pic += '\n'
        return pic

    def __repr__(self):
        """create code to reproduce an object and generate output for developer
        """
        return "Rectangle("+str(self.__width) + ", " + str(self.__height) + ")"

    def __del__(self):
        """delete a rectangle"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
