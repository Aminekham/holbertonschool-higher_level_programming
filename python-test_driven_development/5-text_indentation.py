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
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i])
            print()
        else:
            print(text[i], end="")
