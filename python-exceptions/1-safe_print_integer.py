#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        B = True
    except:
        B = False
    return(B)
