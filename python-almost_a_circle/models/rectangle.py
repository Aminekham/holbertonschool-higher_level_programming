#!/usr/bin/python3
"""
This module represents the rectangle in our new base
"""
from models.base import Base


class Rectangle(Base):
    """
    These are the public attributes of the rectangle
    """
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The init magic method for our class to set the value and use inheret
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return(self.__x)

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return(self.__y)

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculating the area of our rectangle
        """
        return(self.__height * self.__width)

    def display(self):
        """
        display the rectangle
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print("", end=" ")
            for j in range(self.__width):
                if j == self.__width - 1:
                    print("#")
                else:
                    print("#", end="")

    def __str__(self):
        save = f"{self.__width}/{self.__height}"
        return(f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {save}")

    def update(self, *args):
        """
        Update the class attributes with args as input
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.__width = args[1]
                elif i == 2:
                    self.__height = args[2]
                elif i == 3:
                    self.__x = args[3]
                elif i == 4:
                    self.__y = args[4]
