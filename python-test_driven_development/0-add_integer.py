#!/usr/bin/python3
"""
This function is used to test the usage of doctest tool 
Testing cases errors : -a or b are not integers
                       -floats not casting to integers
                       -a or b are extremly large i.e : 1e100, 1e50, 1e10
                       -...
"""
def add_integer(a, b=98):
    """
    add_integer function : function used to test the doctest with an 
    externel .txt file in the tests sub_directory

    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    a, b= int(a), int (b)
    return(a + b)
