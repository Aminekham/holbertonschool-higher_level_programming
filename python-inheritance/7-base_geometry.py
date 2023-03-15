#!/usr/bin/python3
"""
we started with an empty method
"""


class BaseGeometry:
    """
    still working on the area
    adding the validation function
    """
    def area(self):
        pass
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
