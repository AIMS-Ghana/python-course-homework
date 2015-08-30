import math
def root(bisectf, rangex):
 a=rangex[0]
 b=rangex[-1]
 tol=.0001
 while (b-a)>tol:
 #for i in range(a,b):
	  p= float((a+b)/2.0)
	  fp=bisectf(p)
	  if fp==0 or ((b-a)/2)< tol:
	      	  return p
	  #i=i+1
	  if (bisectf(a)*bisectf(p)) > 0:
		 a=p
		 fa=fp
	  else:
	   	b=p 



