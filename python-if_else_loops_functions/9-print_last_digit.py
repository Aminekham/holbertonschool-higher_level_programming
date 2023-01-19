#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        n = -number
    else:
        n = number
    ns = str(n)
    if ns.isnumeric():
        r = ns[len(ns) - 1]
        print("{}".format(r), end = "")
        return(r)
    else:
        return
