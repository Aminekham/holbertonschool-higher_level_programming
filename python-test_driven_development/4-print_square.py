#!/usr/bin/python3
"""
    a module to print a square out of a given size
"""


def print_square(size):
    """
        printing a square of # out of its given size
        testing the legibility of the size
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(1, size * size + 1):
        if i % size == 0:
            print("#")
        else:
            print("#", end="")
