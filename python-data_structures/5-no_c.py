#!/usr/bin/python3
def no_c(my_string):
    newstr = ""
    for ch in (my_string):
        if (ch == 'c' or ch == 'C'):
            newstr+= ''
        else:
            newstr+= ch
    return(newstr)