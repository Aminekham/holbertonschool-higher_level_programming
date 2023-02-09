#!/usr/bin/python3
"""
This module reads a file and prints its content
"""


def read_file(filename=""):
    """
    reading the content of a file using read() method
    """
    with open(filename, 'r', encoding="utf-8") as f:
        x = f.read()
    print(x, end="")
