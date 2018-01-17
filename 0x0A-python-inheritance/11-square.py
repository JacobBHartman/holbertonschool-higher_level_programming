#!/usr/bin/python3
"""this module defines a class called Rectangle"""

class BaseGeometry:
    """this class defines basic geometry objects"""

    def __init__(self):
        """this method is magic and initializes an object
        of class BaseGeometry"""
        pass

    def area(self):
        """this method defines area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this method validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """this class defines rectangles"""

    def __init__(self, width, height):
        """this method is magic and initializes a rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return "[{}] {}/{}".format(type(self).__name__, self.__width, self.__height)

    def area(self):
        """this method defines area"""
        return (self.__width * self.__height)

class Square(Rectangle):
    """this class defines a sub-class of Rectangle: Square"""

    def __init__(self, size):
        """this method is magic and initializes a square"""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[{}] {}/{}".format(type(self).__name__, self.__size, self.__size)

    def area(self):
        """this method defines area"""
        return (self.__size ** 2)
