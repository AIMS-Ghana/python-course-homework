#!/usr/bin/python
import sys
def check(a):
  assert (a>0),"entered negative dimension"

def perimeter(a):
  check(a)
  return (a)*3.14

def area(a):
  check(a)
  return (a*a)*3.14/2

 
if  __name__ =="__main__":
  a = float(sys.argv[1])
  print("area {},\nperimeter {}".format(area(a), perimeter(a))
