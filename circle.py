#!/usr/bin/python

def area(r):
    area_value=math.pi*r**2
    return area_value
def perimeter(r):
    perimeter_value=math.pi*2*r
    return perimeter_value
import sys
import math

if __name__ == "__main__":
    r=float (sys.argv[1])
    print ("area is {}, perimeter is {}".format(area(r), perimeter(r)))
