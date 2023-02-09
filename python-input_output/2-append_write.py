#!/usr/bin/python3
"""
This module appends into a file
"""


def append_write(filename="", text=""):
    """
    using the append file mode
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return(len(text))
