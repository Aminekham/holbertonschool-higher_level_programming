#!/usr/bin/python3
"""
This module writes into a file
"""


def write_file(filename="", text=""):
    """
    using the write file method
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return(len(text))
