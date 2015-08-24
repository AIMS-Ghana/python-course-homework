#!/usr/local/bin/python3

def checkdim(a,b,c):
    assert (a >= 0) & (b >= 0) & (c >= 0), "Passed negative dimensions"
    assert (a+b > c) & (a+c > b) & (b+c > a), "Passed non-triangle dimensions"
    pass


def area(a, b, c):
    checkdim(a,b,c)
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5
    pass


def perimeter(a, b, c):
    checkdim(a,b,c)
    return a+b+c


import sys

if __name__ == "__main__":
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    print("area {}".format(area(a,b,c)))
    print("perimeter {}".format(perimeter(a,b,c)))