#!/usr/bin/python3
"""
This module gives the json representation
"""


def to_json_string(my_obj):
    """
    using the json modules to dump an object into the json format
    """
    import json
    return(json.dumps(my_obj))
