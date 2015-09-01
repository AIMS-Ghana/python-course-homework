#!/usr/bin/python
from random import*
import sys

arg_1=float(sys.argv[1])
arg_2=int(sys.argv[2])

#circle method

a=0
seed(arg_1)
for i in range(arg_2):
	x,y=random(),random()
	r=x**2+y**2	
	if r<=1:
		a+=1
pi_c=(4*a)/float(arg_2)
print "circle area pi:",pi_c

#sphere method
a=0
x,y,z=0,0,0
seed(arg_1)
for i in range(arg_2):
	x,y,z=random(),random(),random()
	r=x**2+y**2+z**2
	if r<=1:
		a+=1
pi_s=(6*a)/float(arg_2)
print "sphere area pi:",pi_s
