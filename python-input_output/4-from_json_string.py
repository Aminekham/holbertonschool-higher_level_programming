#!/usr/bin/python3
"""
This module gives the json representation
"""


def from_json_string(my_str):
    """
    using the json modules to dump an object into the json format
    """
    import json
    return(json.loads(my_str))
