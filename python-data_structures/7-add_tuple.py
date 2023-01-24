#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    s,s1 =len(tuple_a), len(tuple_b)
    x,y,x1,y1 =0, 0, 0, 0
    if s > 0:
        x = tuple_a[0]
    if s > 1:
        y = tuple_a[1]
    if s1 > 0:
        x1 = tuple_b[0]
    if s1 > 1:
        y1 = tuple_b[1]
    return(x+x1, y+y1)
