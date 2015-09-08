#!/usr/bin/python
def checkdim(length,width):
    assert (length >= 0) & (width >= 0), "negative side length"
    pass

def area(length,width):
    checkdim(length,width)
    res=length*width
    return res     

def perimeter(length,width):
    checkdim(length,width)
    return (2*length)+(2*width)
import sys

if __name__=="__main__":
   length=float(sys.argv[1])
   width=float(sys.argv[2]) if (len(sys.argv) == 3) else length

   print("area {},\n perimetre {}".format(area(length,width), perimeter(length,width)))
 
