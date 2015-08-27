#!/usr/bin/python
# A program that prints the area and the perimeter of a triangle.
import sys
a = float(sys.argv[1])
b = float(sys.argv[2])

area = a*b
perimeter = 2*(a*b)


def check(a,b):
    assert (a > 0) & (b > 0) & (len(sys.argv) == 3), "Entered invalid dimension"
    pass

check(a,b)
print "area " + str(area)
print "perimeter " + str(perimeter)


