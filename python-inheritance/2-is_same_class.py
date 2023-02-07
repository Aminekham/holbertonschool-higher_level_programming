#!/usr/bin/python3
"""
this module tells if the object 
"""


def is_same_class(obj, a_class):
    """
        checking using isinstance
    """
    if isinstance(obj, a_class):
        return(True)
    else:
        return(False)
