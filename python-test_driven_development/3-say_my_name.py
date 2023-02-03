#!/usr/bin/python3
"""
a module for saying the name of a person
while testing certain conditions
"""


def say_my_name(first_name="", last_name=""):
    """
        the first and last name will be checked to confirm that their
        type is string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
