#!/usr/bin/python



#integration function
def integrate(f, nbins):

    
    sum = 0.0
    for n in range(nbins-1):  # [0, 1, ... nbins-1]
	width = nbins[n+1] - nbins[n]
	height = f(float(nbins[n+1] + nbins[n])/2)
        sum = sum + width*height

    return sum


