#!/usr/bin/python3
def best_score(a_dictionary):
    x = 0
    y = ""
    if a_dictionary is None or a_dictionary = {}:
        return(None)
    for i in a_dictionary.keys():
        if int(a_dictionary[i]) > x:
            x = int(a_dictionary[i])
            y = i
    return(y)
