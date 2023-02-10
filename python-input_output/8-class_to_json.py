#!/usr/bin/python3
"""
This module return ths dictionary description of a simple data structure
"""


def class_to_json(obj):
    dicts = obj.__dict__
    return(dicts)
