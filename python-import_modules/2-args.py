#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) == 2):
        print("1 argument:")
        print("1: {:s}".format(sys.argv[1]))
    elif (len(sys.argv) == 1):
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(len(sys.argv)-1))
        for i in range(len(sys.argv) - 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
