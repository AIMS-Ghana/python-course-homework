#!/usr/bin/env python3







def f(x):
	return  (x-1)*(x+10)




def bisection(a,b,tol):

	    c = (a+b)/2.0

	    while (b-a)/2.0 > tol:

	        if f(c) == 0:

	            return c

	        elif f(a)*f(c) < 0:

	            b = c

	        else :

	            a = c

	        c = (a+b)/2.0

	         

	    return c

