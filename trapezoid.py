#!/usr/bin/python


def integrate(f,rangex):
	integral  = 0.0
	for n in range(len(rangex)-1):
		a = rangex[n]
		b = rangex[n+1]
		
		height_1 = f(a)
		height_2 = f(b)
		width = b-a
		integral += width*(height_1+height_2)/2
		
	return integral
