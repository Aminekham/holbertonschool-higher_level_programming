#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list
    if idx < 0 :
        return(newlist)
    elif idx > len(newlist):
        return(newlist)
    else:
        x = my_list[idx]
        newlist[idx] = element
        my_list[idx] = x
        return(newlist)