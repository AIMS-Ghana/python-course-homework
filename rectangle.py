#!/usr/bin/python
# A program that prints the area and the perimeter of a triangle.
def check(a,b):
    assert (a > 0) & (b > 0),"Entered nagative dimension"
  

def perimeter(a,b):
    check(a, b)
    return 2*a +2*b

def area(a,b):
    check(a,b)
    res = a*b
    return res

import sys
if __name__ == '__main__':
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print('area {} perimeter {}'.format(area(a,b), perimeter(a, b)))





