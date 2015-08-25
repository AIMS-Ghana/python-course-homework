#!/usr/bin/python3
import sys
import math

def area(r):
 return math.pi*r*r
 

def perimeter(r):
 return 2.0*math.pi*r
 
if __name__ == "__main__":

 if len(sys.argv) == 1:

  print("Input a radius, pal")

 elif len(sys.argv) == 2:

  rad = float(sys.argv[1])
  if rad < 0:

    print("This is negative, pal")

  else:
  
 
  
   print("area:",area(rad))
   print("perimeter:",perimeter(rad))

else:

  print("Too many arguments, pal")

 

 

 

