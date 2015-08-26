#!/usr/bin/python3
import sys
import math


# functions

def area(s1,s2):
     return s1*s2

def perimeter(s1,s2):
     return 2.0*(s1+s2) 

def check(s1,s2):
     assert (s1 > 0) or (s2 > 0), "No negative sides, pal"
   


# scripty bit

if __name__ == "__main__":

 if len(sys.argv) == 1:

  print("Input a side length or two, pal")
  sys.exit(0)

 elif len(sys.argv) == 2:

  s1 = float(sys.argv[1]) 
  s2 = float(sys.argv[1])
  check(s1,s2)
  print("area:",area(s1,s2))
  print("perimeter:",perimeter(s1,s2))
 
  
 elif len(sys.argv) == 3:

  s1 = float(sys.argv[1])
  s2 = float(sys.argv[2])
  check(s1,s2)
  print("area:",area(s1,s2))
  print("perimeter:",perimeter(s1,s2))
 

 else:
  print("Too many arguments, pal")
  sys.exit(0)
  

 

 
  
  



 

 

 

