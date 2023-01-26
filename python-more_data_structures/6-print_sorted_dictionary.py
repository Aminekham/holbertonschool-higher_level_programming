#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    f = sorted(a_dictionary)
    for i in f:
        print("{}: {}".format(i, a_dictionary[i]))
