#!/usr/bin/python3
"""
this module tells if the object is an instance of the class
"""


def is_same_class(obj, a_class):
    """
        checking using isinstance
    """
    if type(obj) is a_class:
        return(True)
    else:
        return(False)
