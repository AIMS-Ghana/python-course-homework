#!/usr/bin/env python



def integrate(f, rangex):
    	toto = 0.0
   	for x in range(len(rangex)-1):
                w = rangex[x+1]-rangex[x]
                h= f(float((rangex[x+1]+rangex[x])/2))
        	area += h*w
	
    	return toto
