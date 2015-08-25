#!/usr/bin/python
import sys
import math

import sys
input_area="{0}"
input_perimeter="{0}"
def area(x):
    area_value=math.pi*float(x)*float(x)
    return area_value
def perimeter(x):
    perimeter_value=math.pi*2*float(x)
    return perimeter_value


if __name__ == "__main__":

    if len(sys.argv) !=2:
        print "wrong inputs"

    else:   
        if sys.argv[1].replace('.','',1).isdigit()==True:
            print "area", area(sys.argv[1])
            print "perimeter", perimeter(sys.argv[1])
        else :
		print "have atleast one value"
