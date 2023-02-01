#!/usr/bin/python3
#!/usr/bin/python3
"""Define an square with size class"""


class Square:
    """Define a private attribute"""
    __size = None

    def __init__(self, size=0):
        if type(size) != int :
            raise TypeError ("size must be an integer")
        if size < 0:
            raise ValueError ("size must be >= 0")
        self.__size = size
