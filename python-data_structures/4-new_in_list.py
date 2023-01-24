#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = []
    if idx < 0 :
        newlist = my_list
        return(newlist)
    elif idx > len(my_list):
        newlist = my_list
        return(newlist)
    else:
        for i in range(len(my_list)):
            if (i == idx):
                newlist.append(element)
            else:
                newlist.append(my_list [i])
        return(newlist)

