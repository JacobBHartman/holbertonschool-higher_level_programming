#!/usr/bin/python3
"""this module divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """
    divides all elements of the matrix

    Args:
        matrix (list): a list of integers or floats
        div (int): the divisor

    Returns:
        a new matrix

    Raises:
        TypeError: if matrix is not a list of ints or floats
        TypeError: if matrix rows are not all the same size
        TypeError: if the divisor is not a number
        ZeroDivisionError: if trying to divide by zero
    """

    # check if matrix is (1) a list (2) of lists (3) of numbers
    errorMsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(errorMsg)
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(errorMsg)
        for j in i:
            if not isinstance(j, float) and not isinstance(j, int):
                raise TypeError(errorMsg)

    # check to make sure each row is the same size
    lng = len(matrix[0])
    for i in matrix:
        if len(i) != lng:
            raise TypeError("Each row of the matrix must have the same size")

    # check to make sure not dividing by zero or non-number
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(list, matrix))
    for g in range(len(new_matrix)):
        for h in range(len(new_matrix[g])):
            new_matrix[g][h] = round(new_matrix[g][h] / div, 2)
    return new_matrix
