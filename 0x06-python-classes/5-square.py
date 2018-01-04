#!/usr/bin/python3
class Square():

    """This is an empty class that defines a square"""

    def __init__(self, size=0):
        """
        __init__ method for the class

        Args:
            size (int): The size of the square.

        """
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = size

    @property
    def size(self):
        """int: gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = value

    def area(self):
        """
        returns the value of the square's area

        Returns:
            the value of the square's area

        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        prints the square

        Returns:
            nothing
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
