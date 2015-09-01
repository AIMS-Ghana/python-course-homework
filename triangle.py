#!/usr/bin/env python3

import sys,math
def check(a,b,c):
	assert a>0& b>0 &c>0

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
#Add two number

summ=(float(a) + float(b) + float(c))
s = (float(a) + float(b) + float(c))/2

#calulate the area
product =(s* (s-float(a) ) * (s-float(b)) * (s-float(c)))**(0.5)
#Displaythe
print('area {}'.format(product))
print('permeter {}'.format(summ))
