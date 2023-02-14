#/usr/bin/python3
"""
This module is the base for the next objects
"""


class Base:
    """
    defining the number of objects and assining id
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id == None:
            self.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
