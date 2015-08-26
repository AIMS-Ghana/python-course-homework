#!/usr/bin/python3
import sys
import math

# functions

def area(r):
 return math.pi*r*r
 

def perimeter(r):
 return 2.0*math.pi*r

def check(r):
 assert r>0,  "No negative radius, pal"

# scripty bit
 
if __name__ == "__main__":

 if len(sys.argv) == 1:

  print("Input a radius, pal")

 elif len(sys.argv) == 2:

  rad = float(sys.argv[1])
  
  check(rad)
  
  print("area:",area(rad))
  print("perimeter:",perimeter(rad))

 else:

  print("Too many arguments, pal")

 

 

 

