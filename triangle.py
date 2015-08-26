#!/usr/bin/python3
import sys
import math

# some functions

def area(a,b,c): 
 s = (a + b + c)/2.0
 return math.sqrt((s-a)*(s-b)*(s-c))

def perimeter(a,b,c):
 return a + b + c

def check(a,b,c):
 assert a>0 and b>0 and c>0,  "No negative sides, pal"
 s = (a+b+c)/2.0 
 assert  s>a and s>b and s>c, "Not a triangle, pal"


# here comes the scripty bit

if __name__ == "__main__":  

 if len(sys.argv) != 4:
  print("Input three side lengths, pal")
 

 else:

  a = float(sys.argv[1])
  b = float(sys.argv[2])
  c = float(sys.argv[3])

  
  check(a,b,c)
   
  print("area:",area(a,b,c))
  print("perimeter:",perimeter(a,b,c))

   

 
  
 

 

 

