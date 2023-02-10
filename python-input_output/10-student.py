#!/usr/bin/python3
"""
This module gives a json repr for our created class
"""


class Student:
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            dic = dict()
            for i in attrs:
                for j in self.__dict__:
                    if i == j:
                        dic[i] = self.__dict__[j]
            return(dic)
        return(self.__dict__)
