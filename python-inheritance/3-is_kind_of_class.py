#!/usr/bin/python3
"""
this module is checking if the obj is an instance of the given class
"""


def is_kind_of_class(obj, a_class):
    """
        using isinstance
    """
    if isinstance(obj, a_class):
        return(True)
    else:
        return(False)
