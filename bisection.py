#!/usr/bin/env python



epsilon = 0.00000000000001
def root(f,rangex):
	l=rangex[0]
	r=rangex[1]
	while abs(l-r)> epsilon :
		x = (l+r)/2.0
		if f(x)== 0 :
			return x
		elif f(l)*f(x)<0 :
   			r=x
		else :
   			l=x
	return x
