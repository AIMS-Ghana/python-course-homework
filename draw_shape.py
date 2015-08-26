#!/usr/bin/python

import sys
import math


def check(name,area):
    #assert (a > 0), "you entered a negative number"
    if name == "TRIANGLE":
        s = 2*(math.sqrt((float(area) / math.sqrt(3))))
        print 'equilateral TRIANGLE, area', area, 'side: ', s

    elif name == "SQUARE":
    	q = math.sqrt(float(area))
        print 'square, area', area, 'side: ', q

    elif name=="CIRCLE":
        # pi=3.14
         r = math.sqrt((float(area)/math.pi))
         print 'CIRCLE, area', area, 'radius: ', r

    else:

         print 'Uknown shape'


#print("Equilateral Triangle, side 4:", side(a))


if __name__ == "__main__":
    check(sys.argv[1],sys.argv[2])


#   if str(sys.argv[1])== triangle.py
