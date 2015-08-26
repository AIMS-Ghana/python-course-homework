#!/usr/bin/python
# A program that prints the area and the perimeter of a triangle.
import math
def check(r):
    assert (r >= 0),"Entered nagative dimension"
  

def perimeter(r):
    check(r)
    return 2*math.pi*r

def area(r):
    check(r)
    res = math.pi*r*r
    return res

import sys
if __name__ == '__main__':
    r = float(sys.argv[1])
    print('area {} perimeter {}'.format(area(r), perimeter(r)))





