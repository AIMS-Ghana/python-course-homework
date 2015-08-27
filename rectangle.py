#!/usr/bin/python
def check(l,w):
  assert (l>0) & (w>0),"entered negative dimension"
def perimeter(l,w):
    check(l,w)
    p=2*(l+w)
    return p

def area(l,w):
   check(l,w)
   t=l*w
   return t

import sys 
if  __name__ =="__main__":
  l = float(sys.argv[1])
  w = float(sys.argv[2])
  
  print("area {},\nperimeter {}".format(area(l,w), perimeter(l,w)))
 
     
    


























