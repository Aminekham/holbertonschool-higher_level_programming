#!/usr/bin/python3
"""
The square class inhereted from the rectangle one
"""


rect = __import__('9-rectangle').Rectangle


class Square(rect):
    """
    the first square class based on rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self._Rectangle__width = size
        self._Rectangle__height = size
        self.__size = size

    def area(self):
        return(self.__size ** 2)
