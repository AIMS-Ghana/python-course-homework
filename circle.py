#!/usr/bin/python 
import math
def check(radius):
    assert (radius > 0), "entered negative radius"

def area(radius):
    check(radius)
    res = (radius**2)*math.pi
    return res
   
def perimeter(radius):
    check(radius)
    return 2*math.pi*radius    
    

import sys
if __name__=="__main__":
   radius=float(sys.argv[1])

   print("area {},\n perimetre {}".format(area(radius), perimeter(radius)))

