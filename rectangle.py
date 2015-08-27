#!/usr/bin/python

def check(a,b):
    assert (a>b)

def perimeter(a,b):
    check(a,b)
    return a+b

def area(a,b):
    check(a,b)
    return a*b

import sys

if __name__ == "__main__":
   a=float (sys.argv[1])
   b=float (sys.argv[2])
print(" area {} \n perimeter {}".format(area(a,b), perimeter(a,b)))


