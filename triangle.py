def check (a,b,c) :
          assert (a>0) & (b>0) & (c>0)  ,"entered negative dimension"
          f=a+b
          d=a-b
          assert (f>c) and (d<c), "violated triangle inequality" 
def perimeter(a,b,c):
	  check (a,b,c)
	  return a+b+c
def area (a,b,c):
	   check (a,b,c)
	   s=(a+b+c)/2
	   ba= s-a
	   bb= s-b
	   bc= s-c
	   area=(s*ba*bb*bc)**0.5 
	   res= area
	   return res

import sys
if __name__ == "__main__":

	  a=float(sys.argv[1])
	  b=float(sys.argv[2])
	  c=float(sys.argv[3])

print("area={}, perimeter={}".format(area(a,b,c),perimeter(a,b,c)))

