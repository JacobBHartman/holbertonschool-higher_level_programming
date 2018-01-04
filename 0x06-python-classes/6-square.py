#!/usr/bin/python3
class Square():

    """This is an empty class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ method for the class

        Attributes:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """int: gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = value

    @property
    def position(self):
        """tuple: gets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        elif position[0] < 0 or position[1] < 0:
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        else:
            self.__position = value

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
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
