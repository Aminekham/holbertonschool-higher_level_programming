#!/usr/bin/python3
"""
This model represents our created square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The init function and the string representation
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return(self.width)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
    def update(self, *args, **kwargs):
        """
        Update the class attributes with args as input
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
        else:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "size" in kwargs.keys():
                self.width = kwargs["size"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]
