#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    addlist=[]
    for i in range(2):
        addlist.append(tuple_a[i] + tuple_b[i])
    newtuple = tuple(addlist)
    return(newtuple)