#!/usr/bin/python



#integration function
def integrate(f, nbins):
    sum_t = 0.0
    for n in range(len(nbins)-1):  # [0, 1, ... nbins-1]
	width = nbins[n+1] - nbins[n]
	midpt = float(nbins[n+1] + nbins[n]/2)
	height = f(midpt)
        sum_t = sum_t + width*height

    return sum_t


