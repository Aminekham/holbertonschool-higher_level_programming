#!/usr/bin/python3
"""
This module prints a sorted list
"""


class MyList(list):
    """
    using the inheritence
    """
    def print_sorted(self):
        print(sorted(self))
