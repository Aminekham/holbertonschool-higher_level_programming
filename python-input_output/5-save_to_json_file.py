#!/usr/bin/python3
"""
write to a json file
"""


def save_to_json_file(my_obj, filename):
    """
    using the json module dump method
    """
    import json
    with open(filename, "w", encoding= "utf-8") as f:
        json.dump(my_obj, f)
