#!/usr/bin/python
def check(length,width):
    assert (length > 0) & (width > 0), "negative side length"
   
def area(length,width):
    check (length,width)
    res=length*width
    return res     

def perimeter(length,width):
    check(length,width)
    return (2*length)+(2*width)
import sys

if __name__=="__main__":
   length=float(sys.argv[1])
   width=float(sys.argv[2])

   print("area {},\n perimetre {}".format(area(length,width), perimeter(length,width)))
 
