#!/usr/bin/python
from math import*
def root(bisecf,l):
	a=l[0]
	b=l[1]
	while b-a>0.0000001:
		m=(a+b)/2.0
		if bisecf(a)*bisecf(m)<0:
			b=m
		elif bisecf(b)*bisecf(m)<0:
			a=m
	return a,b

