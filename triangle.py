#!/usr/bin/python

def check(x,y,z):
 assert x>0 and y>0 and z>0,"Entered a negative dimension."
 m=x+y
 n=x-y
 assert(m>z) and (n<z),"Violated the Triangular inequality."

def area(x,y,z):
 check(x,y,z)
 s=(x+y+z)/2
 res=((s*(s-x)*(s-y)*(s-z))**0.5)
 return res

def perimeter(x,y,z):
 check(x,y,z)
 return x+y+z

import sys

if __name__=="__main__":

 x=float(sys.argv[1])
 y=float(sys.argv[2])
 z=float(sys.argv[3])

print"area " " {}, perimeter" " {}".format(area(x,y,z),perimeter(x,y,z))
