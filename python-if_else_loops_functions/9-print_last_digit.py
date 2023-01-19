#!/usr/bin/python3
def print_last_digit(number):
    ns = str(number)
    if ns.isnumeric():
        r = ns[len(ns) - 1]
        print("{}".format(r), end = "")
        return(r)
    else:
        return
