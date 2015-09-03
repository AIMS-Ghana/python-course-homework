#!/usr/bin/python

def perimeter(a,b,c):
    check(a,b,c)
    p=(a+b+c)
    return p

def area(a,b,c):
    check(a,b,c) 
    p=perimeter(a,b,c)/2
    res=(p*(p-a)*(p-b)*(p-c))**0.5
    return res

def check(a,b,c):
    assert (a>0) & (b>0) & (c>0), "negative dimension"
    s= a+b
    d= a-b
    assert (s>c) and (d<c), "triangle side error"

import sys
if __name__ == "__main__":

    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    print "area {},\nperimeter {}".format(area(a,b,c), perimeter(a,b,c))
