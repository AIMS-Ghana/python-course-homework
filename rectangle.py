#!/usr/bin/python

def area(a,b):
    check(a,b)
    res = a*b
    return res

def perimeter(a,b):
    check(a,b)
    res = 2*(a+b)
    return res

def check(a,b):
    assert (a>0) & (b>0), "entered negative dimension"
import sys 
#input command that does not import sys 
if __name__ =="__main__":

    a = float(sys.argv[1])
    b = float(sys.argv[2])

    print("area{}, perimeter{}".format(area(a,b), perimeter(a,b)))
