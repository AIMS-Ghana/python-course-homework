#!/usr/bin/python

def check(u,v):
    assert (u>0) & (v>0) ,"negative side lenghth"

def area(u,v):
    check(u,v)
    res = u*v
    return res

def perimeter(u,v):
    check(u,v)
    return (2*u)+(2*v)

import sys

if __name__=="__main__":

    u = float(sys.argv[1])
    v = float(sys.argv[2])

print(" area {}, \n perimeter {}".format(area(u,v),perimeter(u,v)))

