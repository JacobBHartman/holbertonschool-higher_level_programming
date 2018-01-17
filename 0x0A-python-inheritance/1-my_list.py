#!/usr/bin/python3
'''this module contains a class MyList that inherits from list'''

class MyList(list):
    '''this class inherits from list'''

    def __init__(self):
        '''this method is magic and initializes a MyList object'''
        super().__init__()

    def print_sorted(self):
        '''this method prints a MyList object, sorted'''
        print(sorted(list(self)))
