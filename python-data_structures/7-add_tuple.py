#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    addlist=[]
    x = len(tuple_a)
    if x > len(tuple_b):
        x = len(tuple_b)
    for i in range(x):
        addlist.append(tuple_a[i] + tuple_b[i])
    newtuple = tuple(addlist)
    return(newtuple)