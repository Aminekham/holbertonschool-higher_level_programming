#!/usr/bin/python3
"""
write to a json file
"""


def load_from_json_file(filename):
    """
    using the json module load method
    """
    import json
    strs = ""
    with open(filename, "r", encoding="utf-8") as f:
        return(json.load(f))
