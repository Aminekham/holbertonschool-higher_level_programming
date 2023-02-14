#!/usr/bin/python3
"""
This module is the base for the next objects
"""


class Base:
    """
    defining the number of objects and assining id
    """
    __nb_objects = 0
    def __init__(self, id=None):
        Base.__nb_objects += 1
        if id != None:
            self.id = id
        else:
            self.id = Base.__nb_objects
