#!/usr/bin/python3
import sys
pi=3.14
def check(r): 
      assert (r>0), "entered negative dimension"
      
def perimeter(r):
       check(r)
       return (2*r*pi)

def area(r):
       check(r)
       res=3.142*r**2
       return res
      

if __name__ ==  "__main__":
  r = float(sys.argv[1])
  print("area {0}, perimeter {1}".format(area(r), perimeter(r)))
