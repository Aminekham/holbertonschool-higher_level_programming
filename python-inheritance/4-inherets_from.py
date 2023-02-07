#!/usr/bin/python3
"""
a module to figure out from what a class inheretes from
"""


def inherits_from(obj, a_class):
    """
    using the issubclass procedure
    """
    if issubclass(obj, a_class):
        return(True)
    else:
        return(False)
