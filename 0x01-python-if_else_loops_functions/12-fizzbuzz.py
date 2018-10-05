#!/usr/bin/python3
'''
    This Python Module contains a method called 'fizzbuzz' that will
    print "Fizz" for multiples of 3, "Buzz for multiples of 5
'''

def fizzbuzz():
    '''
        Well here is the method        
    '''
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(i), end="")
