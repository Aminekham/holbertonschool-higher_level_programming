#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        return(None)
    for i in a_dictionary:
        if i == key:
            del(a_dictionary[key])
            return(a_dictionary)
