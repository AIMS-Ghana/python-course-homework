#!/urs/bin/python

import sys
#import numpy
import scipy
import math

a= float(sys.argv[1]) # getting the inputs
b= float(sys.argv[2])
n= float(sys.argv[3])


def inputs(f,a,b):

    w=(b-a)           #width of rectangle.
    m = (b+a)/2      # getting the midpoints
    h= f(m)           # getting the heights of each point
    area=w*h
    return (area)

# integrating areas

def sum_area(f,n):
    sum=0
    for i in range(len(n)-1):
        sum = sum + math.f(i)
        return sum()


