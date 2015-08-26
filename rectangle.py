#!/usr/bin/env python

#check for negative numbers
def check(x,y):
	assert x>0 and y>0, "please enter a non negative number"

def area(x,y):
    check(x,y)
    area_value=x*y
    return area_value

def perimeter(x,y):
    check (x,y)
    perimeter_value=2*(x+y)
    return perimeter_value

import sys
if __name__ == "__main__":

#calculating for one input / side
 if len(sys.argv)==2:
     x=float(sys.argv[1])	
     #y=float(sys.argv[1])
     print(" area {}, perimeter{}".format(area(x,x), perimeter(x,x)))
 else:
      x=float(sys.argv[1])
      y=float(sys.argv[2])
      print (" area {}, perimeter {}".format(area(x,y), perimeter(x,y)))
   
