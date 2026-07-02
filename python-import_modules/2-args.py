#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    n = len(argv) - 1
    if n == 0:
        print("0 arguments.")
    else:
        if n == 1:
            print("{} argument:".format(n))
        else:
            print("{} arguments:".format(n))
        i = 1
        while i <= n:
            print("{}: {}".format(i, argv[i]))
            i += 1
