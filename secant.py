#!/usr/bin/env python

#Secant method is used to find a root of a function

def root(f, n):
    x=f(n[0])
    y=f(n[1])
    p=y
    for i in range(len(n)):
	if f(x)-f(y)==0:
	   p=y-(f(y)*(y-x))/(f(y)-f(x))
	   x=y
           y=p
	   return p
	    
    

