#!/usr/bin/python3
import sys
import math

def area(s1,s2):
     return s1*s2

def perimeter(s1,s2):
     return 2.0*(s1+s2) 


if __name__ == "__main__":

 if len(sys.argv) == 1:

  print("Input a side length or two, pal")
  sys.exit(0)

 elif len(sys.argv) == 2:

  s1 = float(sys.argv[1]) 
  s2 = float(sys.argv[1])
 
 
  
 elif len(sys.argv) == 3:

  s1 = float(sys.argv[1])
  s2 = float(sys.argv[2])

 

 else:
  
  
   print("Too many arguments, pal")
   sys.exit(0)
  

 if s1 < 0 or s2 <0 :
   print("The side is negative, pal")
   sys.exit(0)

 else:
  
  print("area:",area(s1,s2))
  print("perimeter:",perimeter(s1,s2))



 

 

 

