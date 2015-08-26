def check (L,l) :
          assert (L>0) & (l>0)  ,"entered negative dimension"
       
def perimeter(L,l):
	  check (L,l)
          p=(L+l)*2
	  return p
def area (L,l):
	   check (L,l)
	   area=(L*l) 
	   res= area
	   return res

import sys
if __name__ == "__main__":

	  L=float(sys.argv[1])
	  l=float(sys.argv[2])

print("area={}, perimeter={}".format(area(L,l),perimeter(L,l)))



