#!/usr/bin/python3

def check(a,b):
   assert (a>0) & (b>0), "Negative number entered"
   

def area(a,b):
   check(a,b)
  
   A = a*b
    	
   return A

def perimeter(a,b):
   check(a,b) 
   return 2*(a+b)



import sys

if __name__ == "__main__":
	a = float(sys.argv[1])
	b = float(sys.argv[2])
	print ("area {}, \nperimeter {}".format(area(a,b),perimeter(a,b)))




