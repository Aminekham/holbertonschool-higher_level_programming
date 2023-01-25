#!/usr/bin/python3
def uniq_add(my_list=[]):
    added = []
    x = 0
    for i in range(len(my_list)):
        x = x + my_list[i]
        if my_list[i] in added:
            x = x - my_list[i]
        else:
            added.append(my_list[i])
    return(x)
