#!/usr/bin/python
import sys

def funx(x):
	f=x**3 + x-3
	return f


def root(f,rangex,tol=0.001):
	a=rangex[0]
	b=rangex[1]
	m=(a + b)/2
	
	while (rangex[1]-rangex[0])>tol:
		if f(m) ==0:
			return m
		
	
		elif funx(m)>0:
			b=m
			return m
		elif funx(m)<0:
			a=m
		while f(a)*f(m)<0:
			return m
		else:
			pass
	
		
		


