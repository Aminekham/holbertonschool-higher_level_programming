#!/usr/bin/python3
"""
    a module to check for . ? and : and print two new lines when it finds them
"""


def text_indentation(text):
    """
        checking for ., ? and : while printing the text
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    chars = [".", "?", ":"]
    for char in chars:
        text = text.replace(char, char +"\n\n")
    print(text.strip(), end = "")
