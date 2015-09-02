import math
def check (r) :
          assert (r>0)  ,"entered negative dimension"
       
def perimeter(r):
	  check (r)
          p=(2*r*math.pi)
	  return p
def area (r):
	   check (r)
	   area=(r**2)*math.pi 
	   res= area
	   return res

import sys

if __name__ == "__main__":

	  r=float(sys.argv[1])
	  

print("area={}, perimeter={}".format(area(r),perimeter(r)))



