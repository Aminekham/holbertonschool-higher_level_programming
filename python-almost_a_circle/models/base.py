#!/usr/bin/python3
"""
This module is the base for the next objects
"""


class Base:
    """
    defining the number of objects and assining id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects
    
    def to_json_string(list_dictionaries):
        """
        This method returns the json representation of list_dictionaries variable
        """
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return("[]")
        return(json.dumps(list_dictionaries))
