#!/usr/bin/python


def check(x,y):
 assert x>0 and y>0 ,"Entered a negative dimension"

def area(x,y):
 check(x,y)
 return x*y
def perimeter(x,y):
 check(x,y)
 return 2*(x+y)

import sys

if __name__=="__main__":
#getting the input from the user

 if len(sys.argv)==2:
  x=float(sys.argv[1])
  y=float(sys.argv[1])

  print"area " " {}, perimeter" " {}".format(area(x,y),perimeter(x,y))

 else:
  x=float(sys.argv[1])
  y=float(sys.argv[2])
  print"area " " {}, perimeter" " {}".format(area(x,y),perimeter(x,y))
