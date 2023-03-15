#!/usr/bin/python3
"""

"""


def pascal_triangle(n):
    l = []
    if n <= 0:
        return(l)
    for i in range(n):
        if i == 1 or i == 2:
            l.append(1)
        else:
            l.append()