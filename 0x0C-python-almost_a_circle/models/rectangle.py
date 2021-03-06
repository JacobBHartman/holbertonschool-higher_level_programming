#!/usr/bin/python3
'''
    this module defines a class called Rectangle

    Attributes:
        Public class attributes would go here
'''


from models.base import Base


class Rectangle(Base):
    '''
        a class called Rectangle

        Inherits from:
            Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
            a method that is magic and initializes attributes of a Rectangle

            Args:
                width: width of a rectangle
                height: height of a rectangle
                x: ?? x position of a rectangle ??
                y: ?? y position of a rectangle ??
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
            return the width (private)
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            set the value of width (private)
        '''
        self.validateSetter("width", value)
        self.__width = value

    @property
    def height(self):
        '''
            return the height (private)
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            set the value of height (private)
        '''
        self.validateSetter("height", value)
        self.__height = value

    @property
    def x(self):
        '''
            return the x (private)
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            set the value of x (private)
        '''
        self.validateSetter("x", value)
        self.__x = value

    @property
    def y(self):
        '''
            return the y (private)
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            set the value of y
        '''
        self.validateSetter("y", value)
        self.__y = value

    @staticmethod
    def validateSetter(attribute, value):
        '''
            ensure that any attribute that uses a getter/setter has
            a valid input value
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == 'width' or attribute == 'height':
            if value <= 0:
                raise ValueError("{} must be > 0".format(attribute))
        elif attribute == 'x' or attribute == 'y':
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))

    def area(self):
        '''
            return the value of an area
        '''
        return (self.width * self.height)

    def display(self):
        '''
            print an instance of Rectangle
        '''
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)

    def __str__(self):
        '''
            overload the __str__ magic method with custom output
        '''
        strng = ""
        strng += "[Rectangle] (" + str(self.id) + ") "
        strng += str(self.x) + "/" + str(self.y) + " - "
        strng += str(self.width) + "/" + str(self.height)
        return strng

    def update(self, *args, **kwargs):
        '''
            update the attributes of a rectangle
        '''
        if args is not None and args is not []:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
                return
            except IndexError:
                pass
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def to_dictionary(self):
        '''
            returns the dictionary representation of a Rectangle:
        '''
        custom_dict = {}
        attrs_we_want = ['id', 'width', 'height', 'x', 'y']
        for keys in attrs_we_want:
            custom_dict[keys] = getattr(self, keys)
        return custom_dict
