#!/usr/bin/python3
"""
this is the rectangle class inhereted from the geometry class
"""


base = __import__('7-base_geometry').BaseGeometry


class Rectangle(base):
    """
    the validation and assignment of height and width
    calculating the area with the method area()
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
    def area(self):
        return(self.__height * self.__width)
    def __str__(self):
        return(f"[Rectangle] {self.__width}/{self.__height}")