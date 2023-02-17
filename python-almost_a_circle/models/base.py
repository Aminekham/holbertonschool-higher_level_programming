#!/usr/bin/python3
"""
This module is the base for the next objects
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This method returns the json representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return("[]")
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        The method to save the json format to a .json file
        """
        if list_objs is None:
            list_objs = []
        with open(f"{cls.__name__}.json", "w") as f:
            list_dic = []
            for i in range(len(list_objs)):
                x = list_objs[i]
                d = x.to_dictionary()
                list_dic.append(d)
            s = cls.to_json_string(list_dic)
            f.write(s)

    def from_json_string(json_string):
        """
        This method returns the data structure representation of a json string
        """
        if json_string is None or json_string == "":
            return([])
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            x = cls(1, 1)
        else:
            x = cls(1)
        x.update(**dictionary)
        return(x)
