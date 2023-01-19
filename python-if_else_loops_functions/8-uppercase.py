#!/usr/bin/python3
def uppercase(str):
    f = ""
    for i in range(len(str)):
        if (ord(str[i]) in range(97, 123)):
            f += chr(ord(str[i]) - 32)
        else:
            f += str[i]
    print("{}".format(f))
