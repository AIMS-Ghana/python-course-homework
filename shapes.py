#!/usr/bin/python

import sys
import math
import shapes
import turtle



def check(name,area):
    #assert (a > 0), "you entered a negative number"
    if name == "TRIANGLE":
    # print 'equilateral TRIANGLE, area', area, 'side: ', s
     return 2*(math.sqrt((float(area) / math.sqrt(3))))

    elif name == "SQUARE":
     q = math.sqrt(float(area))
    # print 'square, area', area, 'side: ', q
     return q

    elif name=="CIRCLE":

     r = math.sqrt((float(area)/math.pi))
     #print 'CIRCLE, area', area, 'radius: ', r

     return r

    else:
        print("Uknown shape")


if __name__ == "__main__":
    check(sys.argv[1],sys.argv[2])


def draw_shape.py