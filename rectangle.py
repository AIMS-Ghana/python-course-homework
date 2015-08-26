#!/usr/bin/python3
import sys
def check(a,b):
   assert (a>0) & (b>0),"entered negative dimension"
      
def perimeter(a,b):
  check(a,b)
  return (a+b)*2

def area(a,b):
  check(a,b)
  return (a*b)
      
if __name__ ==  "__main__":
  a = float(sys.argv[1])
  b = float(sys.argv[2])
  print("area {}, perimeter {}".format(area(a,b), perimeter(a,b)))
