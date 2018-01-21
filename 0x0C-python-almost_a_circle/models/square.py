#!/usr/bin/python3
'''
    this module defines a class called Square
'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        A class called Square

        Inherits from:
            Rectangle class which itself inherits from Base class
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
            a method that is magic and initializes attributes of a Square
        '''
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        '''
            return the size (private)
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
            set the value of width (private)
        '''
        self.validateSetter("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        '''
        if args is not None and args is not []:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
                return
            except IndexError:
                pass
        for key in kwargs:
            setattr(self, key, kwargs[key])


    def __str__(self):
        '''
            overload the __str__ magic method with custom output
        '''
        strng = ""
        strng += "[Square] (" + str(self.id) + ") "
        strng += str(self.x) + "/" + str(self.y) + " - "
        strng += str(self.width)
        return strng

    def to_dictionary(self):
        '''
            returns the dictionary representation of a Rectangle:
        '''
        custom_dict = {}
        attrs_we_want = ['id', 'size', 'x', 'y']
        for keys in attrs_we_want:
            custom_dict[keys] = getattr(self, keys)
        return custom_dict

