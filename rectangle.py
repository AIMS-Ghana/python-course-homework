#!/usr/local/bin/python3

def checkdim(a, b):
    assert (a >= 0) & (b >= 0), "Passed negative dimensions"
    pass

def area(a, b):
    checkdim(a, b)
    return a*b

def perimeter(a, b):
    checkdim(a, b)
    return 2*(a+b)

import sys

if __name__ == "__main__":
    a = float(sys.argv[1])
    b = float(sys.argv[2]) if (len(sys.argv) == 3) else a
    print("area {}".format(area(a,b)))
    print("perimeter {}".format(perimeter(a,b)))