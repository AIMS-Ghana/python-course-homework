#!/usr/bin/python3

def check(a,b,c):
   assert (a>0) & (b>0) & (c>0), "Negative number entered"
   s = a + b
   d = a - b
   assert (s>c) & (d<c), "Violated the triangle inequality"

def area(a,b,c):
   check(a,b,c)
   p = (a+b+c)/2
   A = (p*(p-a)*(p-b)*(p-c))**0.5
    	
   return A

def perimeter(a,b,c):
   check(a,b,c) 
   return a+b+c



import sys

if __name__ == "__main__":
	a = float(sys.argv[1])
	b = float(sys.argv[2])
	c = float(sys.argv[3])
	print ("area {}, \nperimeter {}".format(area(a,b,c),perimeter(a,b,c)))




