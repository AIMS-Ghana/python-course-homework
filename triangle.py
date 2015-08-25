#!/usr/bin/python3
import sys
import math

def area(a,b,c): 
 s = (a + b + c)/2.0
 return math.sqrt((s-a)*(s-b)*(s-c))

def perimeter(a,b,c):
 return a + b + c

if __name__ == "__main__":  

 if len(sys.argv) != 4:

  print("Input three side lengths, pal")
 

 else:

  a = float(sys.argv[1])
  b = float(sys.argv[2])
  c = float(sys.argv[3])

  if a < 0 or b<0 or c<0:

   print("No negative sides, pal")
 

  else: 
  
   s = (a+b+c)/2.0 

   if s>a and s>b and s>c:
 
   
    print("area:",area(a,b,c))
    print("perimeter:",perimeter(a,b,c))

   else:

    print("Not a triangle, pal")

 
  
 

 

 

