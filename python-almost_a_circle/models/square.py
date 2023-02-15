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
