#!/usr/bin/python3
import sys
import math
import midpoint
def integrate(f,rangex):
	ss= 0
	for i in range(len(rangex)- 1):
	    h= f((rangex[i+1]+ rangex[i])/2)
	    w= rangex[i+1]-rangex[i]
	    ss = ss + h*w
	return ss
        # get range widths
        #get range midpoints
if __name__ ==" main__":
        print (integrate(lambda x:x, thing))
