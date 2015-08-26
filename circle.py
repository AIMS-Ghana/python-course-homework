#!/usr/bin/python

import math
def area(r):
    check(r)
    res = math.pi*r**2
    return res

def perimeter(r):
    check(r)
    res = 2*math.pi*r
    return res


def check(r):
    assert (r>0), "entered negative dimension"
import sys 
#input command that does not import sys 
if __name__ =="__main__":

    radius = float(sys.argv[1])

    print("area{}, perimeter{}".format(area(radius), perimeter(radius)))



