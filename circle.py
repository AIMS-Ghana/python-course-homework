#!/usr/bin/python
import math
def perimeter(r):
    check(r)
    p=2*math.pi*r
    return p

def area(r):
    check(r) 
    res=math.pi*r**2
    return res

def check(r):
    assert (r>0), "negative dimension"
    

import sys
if __name__ == "__main__":

    radius = float(sys.argv[1])
    print "area {},\nperimeter {}".format(area(radius), perimeter(radius))
