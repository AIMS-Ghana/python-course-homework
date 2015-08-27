#!/usr/bin/python
# A program that prints the area and the perimeter of a triangle.
import math
import sys

def check(a,b,c):
    assert (a > 0) & (b>0) & (c>0), "Entered negative dimension"


def area(a,b,c):
        check(a,b,c)
        s = 0.5*(a+b+c)
        res = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return res

def perimeter(a,b,c):
        check(a,b,c)
        return a+b+c



if __name__ == "__main__":
    if len(sys.argv) == 4:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])

        ar = area(a,b,c)
        pr = perimeter(a,b,c)
        print "area " + str(ar)
        print "perimeter " + str(pr)
    else:
        print 'Error in the number of inputs'