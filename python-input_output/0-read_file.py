#!/usr/bin/python3
"""
This module reads a file and prints its content
"""


def read_file(filename=""):
    """
    reading the content of a file using read() method
    """
    f = open(filename, 'r' , encoding= "utf-8")
    x = f.read()
    print(x, end = "")
