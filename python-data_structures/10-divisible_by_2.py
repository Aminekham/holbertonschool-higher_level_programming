#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    verlist = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            verlist.append(True)
        else:
            verlist.append(False)
    return(verlist)